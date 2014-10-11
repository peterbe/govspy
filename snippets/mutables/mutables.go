package main

import (
	"fmt"
	"strings"
)

func upone_list(thing []string, index int) {
	thing[index] = strings.ToUpper(thing[index])
}

func upone_map(thing map[string]string, index string) {
	thing[index] = strings.ToUpper(thing[index])
}

func main() {
	// mutable
	list := []string{"a", "b", "c"}
	upone_list(list, 1)
	fmt.Println(list) // [a B c]

	// mutable
	dict := map[string]string{
		"a": "anders",
		"b": "bengt",
	}
	upone_map(dict, "b")
	fmt.Println(dict) // map[a:anders b:BENGT]
}
