package main

import "fmt"

func main() {
	var t [5]float64 = [5]float64{24.0, 25.9, 27.8, 26.9, 25.2}

	// 배열 순회
	for i, v := range t { // range : 인덱스, 값 반환
		fmt.Println(i, v)
	}

	// 값만 쓰고 싶을 때
	for _, v := range t {
		fmt.Println(v)
	}
}
