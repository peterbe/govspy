package main

import "fmt"

func main() {
	fmt.Println(`This is
a multi-line string.
`)
	fmt.Println(
		"O'word " +
			"Another \"word\" " +
			"Last word.")
}
