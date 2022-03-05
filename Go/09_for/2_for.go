package main

import "fmt"

func main() {
	i := 0
	// 초기문, 후처리 없어도 가능
	for i < 10 {
		fmt.Print(i, ", ")
		i++
	}
	fmt.Println()
}
