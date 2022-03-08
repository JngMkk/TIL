package main

import (
	"fmt"
	"strings"
)

// 합산할 때마다 새로운 공간 할당 : 문자열이 길어지면 성능 떨어짐
func ToUpper1(str string) string {
	var tmp string
	for _, c := range str {
		if c >= 'a' && c <= 'z' {
			tmp += string('A' + (c - 'a'))
		} else {
			tmp += string(c)
		}
	}
	return tmp
}

// 문자열을 다룰 땐 strings 패키지 찾아보자.
// 새로운 공간을 할당하지 않음
func ToUpper2(str string) string {
	var builder strings.Builder
	for _, c := range str {
		if c >= 'a' && c <= 'z' {
			builder.WriteRune('A' + (c - 'a'))
		} else {
			builder.WriteRune(c)
		}
	}
	return builder.String()
}

func main() {
	var str string = "Hello World"

	fmt.Println(ToUpper1(str))
	fmt.Println(ToUpper2(str))
}
