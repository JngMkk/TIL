package main

import "fmt"

func main() {
	var a float32 = 1234.523
	var b float32 = 3456.1234
	var c float32 = a * b // 4,266,663.334329
	var d float32 = c * 3 // 12,799,990.002987

	fmt.Println(a)
	fmt.Println(b)
	fmt.Println(c) // 4.2666635e+06 -> 4,266,663.5 약 0.2 오차 발생
	fmt.Println(d) // 1.279999e+07 -> 12,799,990.0 약 0.002987 오차 발생
	// 오차가 연산이 거듭될수록 커질 수 있다.
}
