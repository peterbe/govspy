package main

import "fmt"

func main() {
	var symbol string
	fmt.Scanln(&symbol)
	switch symbol {
	case "O":
		fmt.Println("Oxygen")
	case "H":
		fmt.Println("Hydrogen")
	case "He":
		fmt.Println("Helium")
	case "Na":
		fmt.Println("Sodium")
	default:
		fmt.Printf("I have no idea what %s is\n", symbol)
	}

	// Alternative solution

	fmt.Scanln(&symbol)
	db := map[string]string{
		"H":  "Hydrogen",
		"He": "Helium",
		"O":  "Oxygen",
		"Na": "Sodium",
	}
	if name, exists := db[symbol]; exists {
		fmt.Println(name)
	} else {
		fmt.Printf("I have no idea what %s is\n", symbol)
	}

}
