package main

import "fmt"

// for문
// for 초기문; 조건문; 후처리 {
// 	...
// }

// func main() {
// 	for i := 0; i < 10; i++ {
// 		fmt.Print(i, ", ")
// 	}
// 	fmt.Println()
// }

func main() {
	i := 0
	for ; i < 10; i++ {
		fmt.Print(i, ", ")
	}
	fmt.Println()
	fmt.Println(i)
}
