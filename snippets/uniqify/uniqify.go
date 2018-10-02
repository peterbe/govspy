package main

import "fmt"

func uniqify(items []string) []string {
	uniq := make([]string, 0)
	seen := make(map[string]bool)

	// For the highest memory efficiency, do:
	// seen := make(map[string]struct{})
	// see: https://stackoverflow.com/questions/37320287/maptstruct-and-maptbool-in-golang

	for _, i := range items {
		if _, exists := seen[i]; !exists {
			uniq = append(uniq, i)
			seen[i] = true
		}
	}

	return uniq
}

func main() {
	items := []string{"B", "B", "E", "Q", "Q", "Q"}
	items = uniqify(items)
	fmt.Println(items) // prints [B E Q]
}
