package main

import (
	"fmt"
	"math"
)

type Point struct {
	x float64
	y float64
}

func (this Point) distance(other Point) float64 {
	return math.Sqrt(this.x*other.x + this.y*other.y)
}

// since structs get automatically copied, it's better to pass it as pointer
func (this *Point) distance_better(other *Point) float64 {
	return math.Sqrt(this.x*other.x + this.y*other.y)
}

func main() {
	p1 := Point{1, 3}
	p2 := Point{2, 4}
	fmt.Println(p1.distance(p2))         // 3.7416573867739413
	fmt.Println(p1.distance_better(&p2)) // 3.7416573867739413
}
