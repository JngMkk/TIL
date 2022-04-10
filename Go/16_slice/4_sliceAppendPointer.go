package main

import "fmt"

func addNum(slice []int) []int {
	slice = append(slice, 4)
	return slice
}

func addNum2(slice *[]int) {
	*slice = append(*slice, 4)
}

func main() {
	slice := []int{1, 2, 3}
	slice = addNum(slice)

	slice2 := []int{1, 2, 3}
	addNum2(&slice2)

	fmt.Println(slice)
	fmt.Println(slice2)
}
