package main

import (
	"fmt"
	"go/usepkg/custompkg"
	"go/usepkg/exinit"
)

// 패키지 초기화 -> 메인 함수 실행

func main() {
	custompkg.PrintCustom()
	exinit.PrintD()
	fmt.Println("A : ", exinit.A)
}
