package main

import "fmt"

func uniqify(items *[]string) {
	seen := make(map[string]bool)
	j := 0
	for i, x := range *items {
		if !seen[x] {
			seen[x] = true
			(*items)[j] = (*items)[i]
			j++
		}
	}
	*items = (*items)[:j]
}

func main() {
	items := []string{"B", "B", "E", "Q", "Q", "Q"}
	uniqify(&items)
	fmt.Println(items) // prints [B E Q]
}
