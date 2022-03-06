package main

import "fmt"

func main() {
	var a, sum int
	fmt.Scan(&a)
	for i := 1; i < a+1; i++ {
		sum += i
	}
	fmt.Println(sum)
}
