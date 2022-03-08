package main

import "fmt"

func main() {
	str := "Hello 월드"

	// len() : 바이트 길이를 반환
	// 한글은 3byte여서 문자가 이상하게 나옴.
	for i := 0; i < len(str); i++ {
		fmt.Printf("타입 : %T, 값 : %d, 문자값 : %c\n", str[i], str[i], str[i])
	}
	// 타입 : uint8, 값 : 72, 문자값 : H
	// 타입 : uint8, 값 : 101, 문자값 : e
	// 타입 : uint8, 값 : 108, 문자값 : l
	// 타입 : uint8, 값 : 108, 문자값 : l
	// 타입 : uint8, 값 : 111, 문자값 : o
	// 타입 : uint8, 값 : 32, 문자값 :
	// 타입 : uint8, 값 : 236, 문자값 : ì
	// 타입 : uint8, 값 : 155, 문자값 :
	// 타입 : uint8, 값 : 148, 문자값 :
	// 타입 : uint8, 값 : 235, 문자값 : ë
	// 타입 : uint8, 값 : 147, 문자값 :
	// 타입 : uint8, 값 : 156, 문자값 :
}
