package main

import "fmt"

func main() {

	number := 0

	/* It has to be a local variable like this.
	   You can't do `func increment(amount int) {` */
	increment := func(amount int) {
		number += amount
	}
	increment(1)
	increment(2)

	fmt.Println(number) // 3

}
