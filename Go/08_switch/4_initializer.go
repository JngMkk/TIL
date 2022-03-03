package main

// switch 초기문

// switch 초기문; 비굣값 {
// case 값1:
// 	...
// case 값2:
// 	...
// default:
// 	...
// }

import "fmt"

func getMyAge() int {
	return 22
}

func main() {

	switch age := getMyAge(); age {

	case 10:
		fmt.Println("Teenage")

	case 33:
		fmt.Println("Pair 3")

	default:
		fmt.Println("My age is", age)
	}

	// fmt.Println("age is", age)  Error - age 변수는 사라짐(undeclared name)
}
