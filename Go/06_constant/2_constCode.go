package main

import (
	"fmt"
)

// const -> 코드값으로 사용
// 코드란 숫자에 의미를 부여하는 것
// ex) ASCII CODE, UNICODE

const Pig int = 0
const Cow int = 1
const Chicken int = 2

func PrintAnimal(animal int) {
	if animal == Pig {
		fmt.Println("꿀꿀")
	} else if animal == Cow {
		fmt.Println("음메")
	} else if animal == Chicken {
		fmt.Println("꼬끼오")
	} else {
		fmt.Println("...")
	}
}

func main() {
	PrintAnimal(Cow)
	PrintAnimal(Pig)
	PrintAnimal(7)
	PrintAnimal(0)
}
