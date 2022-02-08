package main

import "fmt"

func main() {
	a := 3
	var b float64 = 3.5

	var c int = int(b)

	d := float64(a) * b

	var e int64 = 7
	f := a * int(e)

	fmt.Println(a, b, c, d, e, f)

	// 타입변환 주의사항
	// 큰 타입 -> 작은 타입으로 변환할 때 주의
	var g int16 = 3456   // g는 int16타입 - 2바이트 정수
	var h int8 = int8(g) // int16 -> int8
	fmt.Println(g, h)    // h = -128
}
