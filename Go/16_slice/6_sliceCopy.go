package main

import "fmt"

func main() {
	slice := []int{1, 2, 3, 4, 5}
	slice2 := make([]int, len(slice))

	for i, v := range slice {
		slice2[i] = v
	}

	slice2[1] = 100
	fmt.Println("slice", slice)
	fmt.Println("slice2", slice2)

	slice3 := append([]int{}, slice...)
	slice3[1] = 100
	fmt.Println("slice", slice)
	fmt.Println("slice3", slice3)

	slice4 := make([]int, len(slice))
	copy(slice4, slice)
	slice4[1] = 100
	fmt.Println("slice", slice)
	fmt.Println("slice4", slice4)
}
