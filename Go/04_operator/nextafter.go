package main

import (
	"fmt"
	"math"
)

func equal(a, b float64) bool {
	return math.Nextafter(a, b) == b // Nextafter(a, b) a에서 b로 1bit 만큼 간다
}

func main() {
	var a float64 = 0.1
	var b float64 = 0.2
	var c float64 = 0.3

	fmt.Printf("%0.18f == %0.18f : %v\n", c, a+b, equal(a+b, c))
}
