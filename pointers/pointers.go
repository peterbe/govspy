package main

import "fmt"

func double(thing int) {
	thing = thing * 2
}

func double2(thing *int) {
	*thing = *thing * 2
}

func main() {
	number := 5
	double(number)
	fmt.Println(number) // 5

	double2(&number)
	fmt.Println(number) // 10
}
