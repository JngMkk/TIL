package main

import "fmt"

/*
변수란?

값을 저장하는 메모리 공간을 가리키는 이름
*/

func main() {
	// var : 변수 선언
	// var {변수명} {변수타입}
	// 모든 정수 타입, 모든 실수 타입 기본값 : 0
	// bool 기본값 false
	// 문자열 ""(빈 문자열)
	// 그 외 nil(정의되지 않은 메모리 주소를 나타냄)
	// 연산의 각 항목의 타입은 반드시 같아야 함.
	var a int = 10
	b := 30
	var c = "Hi"
	d := 3.14
	var e float64 = 1.1
	var msg string = "Hello Variable"
	fmt.Println(msg, a, b, c, d, e)

	a = 20
	msg = "Good Morning"
	fmt.Println(msg, a, b, c, d, e)
}
