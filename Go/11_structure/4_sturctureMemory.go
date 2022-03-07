package main

import (
	"fmt"
	"unsafe"
)

type User struct {
	Age   int32   // 4byte
	Score float64 // 8byte
}

func main() {
	var a int = 8
	user := User{23, 77.2}
	fmt.Println(unsafe.Sizeof(user), unsafe.Sizeof(a))
	// 변수의 메모리 크기를 반환 16? why? -> 메모리 정렬 ( 실제 배치 : 64비트 컴퓨터면 8바이트로 정렬 레지스터에 담기 편하기 하기 위해 , 8의 배수가 값이 편함 )
	// memory alignment, memory padding
}
