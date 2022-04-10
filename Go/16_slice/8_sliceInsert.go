package main

import "fmt"

func main() {
	slice := []int{1, 2, 3, 4, 5, 6}
	slice = append(slice, 0)
	idx := 2

	for i := len(slice) - 2; i >= idx; i-- {
		slice[i+1] = slice[i]
	}

	slice[idx] = 100
	fmt.Println(slice)

	slice2 := []int{1, 2, 3, 4, 5, 6}
	// 불필요한 메모리 할당이 될 수 있다.
	slice2 = append(slice2[:idx], append([]int{100}, slice2[idx:]...)...)
	fmt.Println(slice2)

	slice3 := []int{1, 2, 3, 4, 5, 6}
	slice3 = append(slice3, 0)
	copy(slice3[idx+1:], slice3[idx:])
	slice3[idx] = 100
	fmt.Println(slice3)
}
