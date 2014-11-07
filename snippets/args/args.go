package main

import (
	"fmt"
	"os"
	"strings"
)

func transform(args []string) {
	for _, arg := range args {
		fmt.Println(strings.ToUpper(arg))
	}

}
func main() {
	args := os.Args[1:]
	transform(args)
}
