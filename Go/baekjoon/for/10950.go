package main

import "fmt"

func main() {
	var a, b, c int
	fmt.Scan(&c)
	for i := 0; i < c; i++ {
		fmt.Scan(&a, &b)
		fmt.Println(a + b)
	}
}
