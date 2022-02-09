package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	stdin := bufio.NewReader(os.Stdin)

	var a int
	var b int

	n, err := fmt.Scanln(&a, &b)
	// nil : 올바르지 않은 메모리 주소
	if err != nil {
		// 에러가 있다면
		fmt.Println(err)
		stdin.ReadString('\n') // 개행 문자가 나올 때까지 읽어와라
	} else {
		fmt.Println(n, a, b)
	}

	n, err = fmt.Scanln(&a, &b)
	// nil : 올바르지 않은 메모리 주소
	if err != nil {
		// 에러가 있다면
		fmt.Println(err)
		stdin.ReadString('\n') // 개행 문자가 나올 때까지 읽어와라
	} else {
		fmt.Println(n, a, b)
	}
}
