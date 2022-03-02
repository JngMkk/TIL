package main

import (
	"fmt"
)

func main() {
	const pi1 float64 = 3.141592653  // 상수
	var pi2 float64 = 3.141592653589 // 변수

	// 상수 선언
	// const ConstValue int = 10
	// 값을 바꿀 수 없다

	// pi1 = 3 -> cannot assign to pi1 (declared const)
	pi2 = 4

	fmt.Printf("원주율: %f\n", pi1)
	fmt.Printf("원주율: %f\n", pi2)
}
