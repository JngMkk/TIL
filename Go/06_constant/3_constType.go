package main

import "fmt"

// 상수는 좌변으로 사용할 수 없다(메모리 공간이 없다. 값으로만 쓰임)
const PI = 3.14
const FloatPI float64 = 3.14

func main() {
	var a int = PI * 100
	// var b int = FloatPI * 100 -> 타입오류 발생

	fmt.Println(a)
}
