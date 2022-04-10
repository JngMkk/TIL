package main

import "fmt"

func main() {
	slice := []int{1, 2, 3, 4, 5, 6}
	idx := 2

	for i := idx + 1; i < len(slice); i++ {
		slice[i-1] = slice[i]
	}

	slice = slice[:len(slice)-1]

	fmt.Println("slice", slice)

	slice2 := []int{1, 2, 3, 4, 5, 6}
	slice2 = append(slice2[:idx], slice2[idx+1:]...)
	fmt.Println("slice2", slice2)

	slice3 := []int{1, 2, 3, 4, 5, 6}
	copy(slice3[idx:], slice3[idx+1:])
	slice3 = slice[:len(slice3)-1]
	fmt.Println("slice3", slice3)
}
