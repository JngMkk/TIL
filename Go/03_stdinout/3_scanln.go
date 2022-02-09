package main

import "fmt"

func main() {
	// Scan은 Print와 마찬가지로 Scan(), Scanf(), Scanln()이 있음
	// func Scanln(a ...interface{}) (n int, err error)
	// 두 개의 값을 출력함 (n, err)
	var a int
	var b int
	n, err := fmt.Scanln(&a, &b) // & : 변수의 메모리 주소값에 입력받은 값을 넣겠다.
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println(n, a, b)
	}
}
