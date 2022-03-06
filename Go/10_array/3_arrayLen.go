package main

import "fmt"

func main() {
	nums := [...]int{10, 20, 30, 40, 50} // [5]int{10, 20, ...}

	nums[2] = 300

	// 배열 순회
	for i := 0; i < len(nums); i++ {
		fmt.Println(nums[i])
	}
}
