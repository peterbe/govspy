package main

import "fmt"

func main() {
	// initialized array
	var numbers [5]int // becomes [0, 0, 0, 0, 0]
	// change one of them
	numbers[2] = 100
	// create a new slice from an array
	some_numbers := numbers[1:3]
	fmt.Println(some_numbers) // [0, 100]
	// length of it
	fmt.Println(len(numbers))

	// initialize a slice
	var scores []float64
	scores = append(scores, 1.1) // recreate to append
	scores[0] = 2.2              // change your mind
	fmt.Println(scores)          // prints [2.2]

	// when you don't know for sure how much you're going
	// to put in it, one way is to
	var things [100]string
	things[0] = "Peter"
	things[1] = "Anders"
	fmt.Println(len(things)) // 100
}
