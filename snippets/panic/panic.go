package main

import "fmt"

func main() {
	// Running this will print out:
	//    error was: Shit!
	defer func() {
		fmt.Println("error was:", recover())
	}()
	panic("Shit!")
}
