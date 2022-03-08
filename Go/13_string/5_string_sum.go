package main

import "fmt"

func main() {
	// 문자열의 변수는 주소값을 가리키는 포인터다..!
	// str1 : Data | Len ( 100 | 5 )
	str1 := "Hello"
	str2 := "World"
	str3 := str1 + " " + str2
	fmt.Println(str3)

	str1 += " " + str2
	fmt.Println(str1)
}
