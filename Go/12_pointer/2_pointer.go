package main

import "fmt"

func main() {
	var a int = 10
	var b int = 20

	// 포인터 변수의 기본값은 nil
	var p1, p2 *int = &a, &a
	var p3 *int = &b

	fmt.Printf("p1 == p2: %v\n", p1 == p2)
	fmt.Printf("p2 == p3: %v\n", p2 == p3)
}
