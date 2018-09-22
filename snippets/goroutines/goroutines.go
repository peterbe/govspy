package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"sync"
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

// See the example in https://golang.org/pkg/sync/#WaitGroup
func main() {
	var wg sync.WaitGroup
	urls := []string{
		"http://www.peterbe.com",
		"http://peterbe.com",
		"http://htmltree.peterbe.com",
		"http://tflcameras.peterbe.com",
	}
	for _, url := range urls {
		wg.Add(1)
		go func(url string) {
			defer wg.Done()
			f(url)
		}(url)
	}
	// Wait for the goroutines to finish
	wg.Wait()
}
