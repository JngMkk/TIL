package main

import "fmt"

// main 아래 있어도 가능
func Add(a int, b int) int {
	return a + b
}

func main() {
	c := Add(3, 6)
	d := Sub(6, 3)
	fmt.Println(c)
	fmt.Println(d)
}

func Sub(a int, b int) int {
	return a - b
}
