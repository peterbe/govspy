package main

import "fmt"

func main() {
	max := 10
	panic(fmt.Sprintf("The max. number is %d", max))
}
