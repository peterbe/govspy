package main

import "fmt"

func main() {
	names := []string{"peter", "anders", "bengt", "bengtsson"}
	initials := make(map[string]int)
	for _, name := range names {
		initial := string(name[0])
		initials[initial]++
	}
	fmt.Println(initials)
	// outputs
	// map[p:1 a:1 b:2]
}
