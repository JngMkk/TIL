package main

import "fmt"

func main() {
	for i := 0; i < 10; i++ {
		if i == 3 {
			continue // 후처리로 건너 뜀
		}
		if i == 6 {
			break
		}
		fmt.Println("6 *", i, "=", 6*i)
	}
}
