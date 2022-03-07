package main

import (
	"fmt"
	"unsafe"
)

type User struct {
	A int8 // 1byte
	B int  // 8byte
	C int8 // 1byte
	D int  // 8btye
	E int8 // 1byte
}

type User2 struct {
	A int8
	C int8
	E int8
	// 8바이트보다 작은 필드는 8바이트 크기를 고려해서 몰아서 배치하자.
	B int
	D int
}

func main() {
	user := User{1, 2, 3, 4, 5}
	user2 := User2{1, 2, 3, 4, 5}
	fmt.Println(unsafe.Sizeof(user))  // 40btye
	fmt.Println(unsafe.Sizeof(user2)) // 24byte
}
