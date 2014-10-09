package main

import (
	"os"
)

func main() {
	f, _ := os.Open("defer.py")
	defer f.Close()
	// you can now read from this
	// `f` thing and it'll be closed later

}
