package main

import "fmt"

func canIDrink(age int) bool {
	defer fmt.Println("Done!")
	switch age {
	case 10:
		return false
	case 18:
		return true
	}
	return false
}

func main() {
	fmt.Println(canIDrink(18))
}
