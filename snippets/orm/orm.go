package main

import (
	"database/sql"
	"errors"
	"fmt"
	"github.com/coopernurse/gorp"
	_ "github.com/lib/pq"
	"log"
	"math/rand"
	// "os"
	"regexp"
	"strings"
	"time"
)

type StringSlice []string

// Implements sql.Scanner for the String slice type
// Scanners take the database value (in this case as a byte slice)
// and sets the value of the type.  Here we cast to a string and
// do a regexp based parse
func (s *StringSlice) Scan(src interface{}) error {
	asBytes, ok := src.([]byte)
	if !ok {
		return error(errors.New("Scan source was not []bytes"))
	}

	asString := string(asBytes)
	parsed := parseArray(asString)
	(*s) = StringSlice(parsed)

	return nil
}

func ToArray(str []string) string {
	L := len(str)
	out := "{"
	for i, s := range str {
		out += "\"" + s + "\""
		if i+1 < L {
			out += ","
		}
	}
	out += "}"

	return out
}

// construct a regexp to extract values:
var (
	// unquoted array values must not contain: (" , \ { } whitespace NULL)
	// and must be at least one char
	unquotedChar  = `[^",\\{}\s(NULL)]`
	unquotedValue = fmt.Sprintf("(%s)+", unquotedChar)

	// quoted array values are surrounded by double quotes, can be any
	// character except " or \, which must be backslash escaped:
	quotedChar  = `[^"\\]|\\"|\\\\`
	quotedValue = fmt.Sprintf("\"(%s)*\"", quotedChar)

	// an array value may be either quoted or unquoted:
	arrayValue = fmt.Sprintf("(?P<value>(%s|%s))", unquotedValue, quotedValue)

	// Array values are separated with a comma IF there is more than one value:
	arrayExp = regexp.MustCompile(fmt.Sprintf("((%s)(,)?)", arrayValue))

	valueIndex int
)

// Find the index of the 'value' named expression
func init() {
	for i, subexp := range arrayExp.SubexpNames() {
		if subexp == "value" {
			valueIndex = i
			break
		}
	}
}

// Parse the output string from the array type.
// Regex used: (((?P<value>(([^",\\{}\s(NULL)])+|"([^"\\]|\\"|\\\\)*")))(,)?)
func parseArray(array string) []string {
	results := make([]string, 0)
	matches := arrayExp.FindAllStringSubmatch(array, -1)
	for _, match := range matches {
		s := match[valueIndex]
		// the string _might_ be wrapped in quotes, so trim them:
		s = strings.Trim(s, "\"")
		results = append(results, s)
	}
	return results
}

const HOW_MANY = 1000

func random_topic() string {
	topics := []string{
		"No talks added yet",
		"I'm working on a branch of django-mongokit that I thought you'd like to know about.",
		"I want to learn Gaelic.",
		"I'm well, thank you.",
		"(Kaw uhn KEU-ra shin KAW-la root uh CHOO-nik mee uhn-royer?)",
		"Chah beh shin KEU-ra, sheh shin moe CHYEH-luh uh vah EEN-tchuh!",
		"STUH LUH-oom BRISS-kaht-chun goo MAWR",
		"Suas Leis a' Ghàidhlig! Up with Gaelic!",
		"Tha mi ag iarraidh briosgaid!",
	}

	return topics[rand.Intn(len(topics))]
}

func random_when() time.Time {
	return time.Date(
		2000+rand.Intn(10),
		time.November,
		rand.Intn(12),
		rand.Intn(28),
		0, 0, 0, time.UTC)
}

func random_tags() []string {
	tags := []string{
		"one",
		"two",
		"three",
		"four",
		"five",
		"six",
		"seven",
		"eight",
		"nine",
		"ten",
	}
	return tags[:rand.Intn(4)]
}

func random_duration() float64 {
	return rand.Float64() * 10
}

func main() {
	dbmap := initDb()
	defer dbmap.Db.Close()

	// alter sequence talks_id_seq restart with 1;

	err := dbmap.TruncateTables()
	checkErr(err, "TruncateTables failed")

	// dbmap.TraceOn("[gorp]", log.New(os.Stdout, "myapp:", log.Lmicroseconds))

	t0 := time.Now()
	var talks [HOW_MANY]Talk

	trans, err := dbmap.Begin()
	if err != nil {
		panic(err)
	}
	// CREATE
	for i := 0; i < HOW_MANY; i++ {
		topic := random_topic()
		when := random_when()
		tags := random_tags()
		duration := random_duration()

		talk := Talk{
			Topic:    topic,
			When:     when,
			Tags:     ToArray(tags),
			Duration: duration,
		}

		err = dbmap.Insert(&talk)
		checkErr(err, "Insert failed")
		talks[i] = talk

	}

	trans.Commit()
	t1 := time.Since(t0)
	t0 = time.Now()

	trans, err = dbmap.Begin()
	if err != nil {
		panic(err)
	}

	// EDIT ALL
	for _, talk := range talks {

		talk.Topic += "extra"
		talk.Duration += 1.0
		talk.When = talk.When.Add(time.Hour * 24)
		tags := parseArray(talk.Tags)
		talk.Tags = ToArray(append(tags, "extra"))

		_, err := dbmap.Update(&talk)
		checkErr(err, "Update failed")
	}

	trans.Commit()
	t2 := time.Since(t0)
	t0 = time.Now()

	trans, err = dbmap.Begin()
	if err != nil {
		panic(err)
	}

	// DELETE ALL
	for _, talk := range talks {
		_, err = dbmap.Exec("delete from talks where id=$1", talk.Id)
		checkErr(err, "Delete failed")
	}

	trans.Commit()
	t3 := time.Since(t0)

	fmt.Println("insert", t1)
	fmt.Println("edit", t2)
	fmt.Println("delete", t3)
	fmt.Println("TOTAL", t1+t2+t3)

}

type Talk struct {
	// db tag lets you specify the column name
	// if it differs from the struct field
	Id    int64     `db:"id"`
	Topic string    `db:"topic"`
	When  time.Time `db:"when"`
	// Tags    StringSlice
	Tags     string  `db:"tags"`
	Duration float64 `db:"duration"`
}

func initDb() *gorp.DbMap {
	// connect to db using standard Go database/sql API
	// use whatever database/sql driver you wish
	db, err := sql.Open("postgres", `
		user=peterbe dbname=fastestdb
		password=test123 sslmode=disable`)
	checkErr(err, "sql.Open failed")

	// construct a gorp DbMap
	dbmap := &gorp.DbMap{Db: db, Dialect: gorp.PostgresDialect{}}

	// add a table, setting the table name to 'talks' and
	// specifying that the Id property is an auto incrementing PK
	dbmap.AddTableWithName(Talk{}, "talks").SetKeys(true, "Id")

	return dbmap
}

func checkErr(err error, msg string) {
	if err != nil {
		log.Fatalln(msg, err)
	}
}
