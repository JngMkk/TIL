package main

import "fmt"

// 배열은 연속된 메모리
// 요소 위치 = 배열 시작 주소 + (index * 타입 크기)
// Random Access : 배열이 가장 빠르다(연속된 메모리 형태이기 때문)

// 배열 복사
func main() {
	a := [5]int{1, 2, 3, 4, 5}
	b := [5]int{500, 400, 300, 200, 100}

	for i, v := range a {
		fmt.Printf("a[%d] = %d\n", i, v)
	}

	fmt.Println()

	for i, v := range b {
		fmt.Printf("b[%d] = %d\n", i, v)
	}

	b = a // 값 타입크기를 복사(메모리 전체가 복사된다 -> 타입 크기가 같아야 한다.)

	fmt.Println()

	for i, v := range b {
		fmt.Printf("b[%d] = %d\n", i, v)
	}
}
