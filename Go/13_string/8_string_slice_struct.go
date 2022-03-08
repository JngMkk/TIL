package main

import (
	"fmt"
	"reflect"
	"unsafe"
)

func main() {
	// 문자는 불변.
	str := "Hello World"
	// 다른 공간에 복사한다.
	slice := []byte(str)

	stringHeader := (*reflect.StringHeader)(unsafe.Pointer(&str))
	sliceHeader := (*reflect.SliceHeader)(unsafe.Pointer(&slice))

	fmt.Printf("str:\t%x\n", stringHeader.Data)
	fmt.Printf("slice:\t%x\n", sliceHeader.Data)
}
