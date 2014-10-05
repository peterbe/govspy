package main

import (
	"fmt"
	"strconv"
)

func str2int(s string) int {
	i, err := strconv.Atoi(s)
	if err != nil {
		panic("Not a number")
	}
	return i
}

func main() {
	var number_string string
	fmt.Scanln(&number_string)
	number := str2int(number_string)

	switch number {
	case 8:
		fmt.Println("Oxygen")
	case 1:
		fmt.Println("Hydrogen")
	case 2:
		fmt.Println("Helium")
	case 11:
		fmt.Println("Sodium")
	default:
		fmt.Printf("I have no idea what %d is\n", number)
	}

	// Alternative solution

	fmt.Scanln(&number_string)
	db := map[int]string{
		1:  "Hydrogen",
		2: "Helium",
		8:  "Oxygen",
		11: "Sodium",
	}
	number = str2int(number_string)
	if name, exists := db[number]; exists {
		fmt.Println(name)
	} else {
		fmt.Printf("I have no idea what %d is\n", number)
	}

}
