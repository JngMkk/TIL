package main

import "fmt"

var cnt int = 0 // global variable(패키지 전역변수)

func IncreaseAndReturn() int {
	fmt.Println("IncreaseAndReturn()", cnt)
	cnt++
	return cnt
}

func main() {
	// 쇼트서킷 : && 연산자에서 앞에 것이 false이면 두 번째 것은 검사하지 않고(무시하고) 바로 false
	// || 연산자에서 앞에 것이 true이면 두 번째 것은 검사하지 않고(무시하고) 바로 true
	if false && IncreaseAndReturn() < 5 {
		fmt.Println("1 증가") // 쇼트서킷때문에 출력되지 않음 false라서 무시
	}
}
