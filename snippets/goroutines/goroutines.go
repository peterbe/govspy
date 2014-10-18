package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
)

func f(url string) {
	response, err := http.Get(url)
	if err != nil {
		panic(err)
	}
	defer response.Body.Close()
	body, err := ioutil.ReadAll(response.Body)
	if err != nil {
		panic(err)
	}

	fmt.Println(len(body))
}

func main() {
	urls := []string{
		"http://www.peterbe.com",
		"http://peterbe.com",
		"http://htmltree.peterbe.com",
		"http://tflcameras.peterbe.com",
	}
	for _, url := range urls {
		go f(url)
	}
	// necessary so it doesn't close before
	// the goroutines have finished
	var input string
	fmt.Scanln(&input)
}
