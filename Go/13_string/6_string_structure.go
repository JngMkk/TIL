package main

import (
	"fmt"
	"reflect"
	"unsafe"
)

func main() {
	str1 := "Hello 월드"
	str2 := str1

	stringHeader1 := (*reflect.StringHeader)(unsafe.Pointer(&str1)) // &str1 : str1의 메모리 주소값을 unsafe패키지의 pointer 타입으로(내부 raw pointer로)
	stringHeader2 := (*reflect.StringHeader)(unsafe.Pointer(&str2))

	fmt.Println(stringHeader1)
	fmt.Println(stringHeader2)
	// &{4807054 12} : Data(실제 메모리 주소) | Len(Byte 길이)
	// &{4807054 12}
}
