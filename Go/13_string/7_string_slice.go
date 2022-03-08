package main

import (
	"fmt"
)

func main() {
	// string의 일부만 바꿀 수 없음
	var str string = "Hello World"
	var slice []byte = []byte(str)
	tmp := []rune(str)

	slice[2] = 'a'
	tmp[2] = 'a'

	fmt.Println(str)
	fmt.Printf("%s\n", slice)
	for _, v := range tmp {
		fmt.Printf("%c", v)
	}
	fmt.Println()
}
