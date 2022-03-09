package main

import (
	"fmt"
	"go/usepkg/custompkg"

	"github.com/guptarohit/asciigraph"
	"github.com/tuckersGo/musthaveGo/ch16/expkg"
)

// go mod init
// go mod tidy -> 외부 패키지 다운로드
// 프로그램 있는 디렉터리에서 go build
// go env -> 패키지 다운로드 경로(GOPATH)

func main() {
	custompkg.PrintCustom()
	custompkg.Print2()
	// custompkg.printcustom2() 외부로 공개되지 않은 함수 cannot refer to unexported name custompkg.printcustom2
	s := custompkg.Student{}
	s.Name = "Go"
	s.Age = 32
	// s.score = 100  외부로 공개되지 않음 s.score undefined (cannot refer to unexported field or method score)

	fmt.Println(s.Name, s.Age)
	fmt.Println(custompkg.PI)
	custompkg.Ratio = 10
	fmt.Println(custompkg.Ratio)

	expkg.PrintSample()

	data := []float64{3, 4, 5, 6, 9, 7, 5, 8, 5, 10, 2, 7, 2, 5, 6}
	graph := asciigraph.Plot(data)
	fmt.Println(graph)
	fmt.Println()
}
