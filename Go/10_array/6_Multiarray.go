package main

import "fmt"

func main() {
	a := [2][5]int{
		{1, 2, 3, 4, 5},
		{5, 6, 7, 8, 9}, // 같을 줄에서 닫히면 , 생략 가능 but 다른 줄에서 닫히면 , 찍어줘야 함
	}

	for _, arr := range a {
		for _, v := range arr {
			fmt.Print(v, " ")
		}
		fmt.Println()
	}
}
