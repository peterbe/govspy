package main

import "fmt"

func main() {
	elements := make(map[string]int)
	elements["H"] = 1
	fmt.Println(elements["H"])

	// remove by key
	elements["O"] = 8
	delete(elements, "O")

	// only do something with a element if it's in the map
	if number, ok := elements["O"]; ok {
		fmt.Println(number) // won't be printed
	}
	if number, ok := elements["H"]; ok {
		fmt.Println(number) // 1
	}

}
