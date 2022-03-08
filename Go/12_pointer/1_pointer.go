package main

import "fmt"

// 포인터 : 메모리 주소를 값으로 갖는 타입
// var a int
// var p *int
// p = &a // a의 메모리 주소를 포인터 변수 p에 대입함.
// *p = 20 // p가 가리키는 공간의 값을 20으로 바꿔라.
// 여러 포인터 변수가 하나의 변수를 가리킬 수 있다.
func main() {
	var a int = 500
	var p *int

	p = &a

	fmt.Printf("p의 메모리 주소값 : %p\n", p) // 16진수 값
	fmt.Printf("p가 가리키는 메모리의 실제값 : %d\n", *p)

	*p = 100 // a = 100
	fmt.Printf("a의 실제값 : %d\n", a)
}
