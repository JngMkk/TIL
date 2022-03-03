package main

import "fmt"

func main() {
	var age = 22

	if age >= 10 && age <= 15 {
		fmt.Println("U r young")
	} else if age > 30 || age < 20 {
		fmt.Println("U r not 20s")
	} else {
		fmt.Println("Best age")
	}
}
