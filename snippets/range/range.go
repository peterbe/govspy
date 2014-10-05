package main

import "fmt"

func main() {
	names := []string{
		"Peter",
		"Anders",
		"Bengt",
	}
	/* This will print

	1. Peter
	2. Anders
	3. Bengt
	*/
	for i, name := range names {
		fmt.Printf("%d. %s\n", i+1, name)
	}
}
