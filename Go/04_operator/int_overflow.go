package main

import "fmt"

func main() {
	var x int8 = 127
	fmt.Printf("%d < %d+1: %v\n", x, x, x < x+1) // false
	fmt.Printf("x = %4d, %08b\n", x, x)
	fmt.Printf("x+1 = %4d, %08b\n", x+1, uint8(x+1))
}
