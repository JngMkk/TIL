package main

import "fmt"

func main() {
	str := "Hello 월드"
	// slice(동적 배열)
	// rune : int32의 별칭 타입
	// 한 칸이 4byte <- UTF-8 담을 수 있음
	// 동적 배열로만 가능
	arr := []int32(str)
	arr2 := []rune(str)

	for i := 0; i < len(arr); i++ {
		fmt.Printf("타입 : %T, 값 : %d, 문자값 : %c\n", arr[i], arr[i], arr[i])
	}

	fmt.Println()

	for i := 0; i < len(arr2); i++ {
		fmt.Printf("타입 : %T, 값 : %d, 문자값 : %c\n", arr2[i], arr2[i], arr2[i])
	}
}
