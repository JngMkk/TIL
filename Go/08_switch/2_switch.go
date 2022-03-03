package main

import "fmt"

func main() {
	// 한번에 여러 값 비교
	day := "thursday"

	switch day {
	case "monday", "tuesday":
		fmt.Println("월, 화요일은 수업을 가는 날입니다.")
	case "Wednesday", "thursday", "friday":
		fmt.Println("수, 목, 금요일은 실습을 가는 날입니다.")
	}
}
