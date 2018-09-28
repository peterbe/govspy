package main


import "fmt"
import "time"

func main() {
	t0 := time.Now()
	elapsed := time.Since(t0)
	fmt.Printf("Took %s", elapsed)
}
