package main

import "fmt"

// pacakge global variable
var g int = 10

func main() {
	var m int = 20

	{
		var s int = 50
		fmt.Println(m, s, g)
	}

	// 중괄호 밖을 벗어나면 s 변수가 사라짐
	m = s + 20 // undeclared name
}
