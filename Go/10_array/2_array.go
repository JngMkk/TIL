package main

const Y int = 3

// 배열 선언시 개수는 항상 상수

func main() {
	x := 5
	a := [x]int{1, 2, 3, 4, 5}	// 에러
	b := [Y]int{1, 2, 3}	// 에러 x
	var c [10]int	// 에러 x
}