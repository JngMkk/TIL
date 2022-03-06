package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var a, b int
	stdin := bufio.NewReader(os.Stdin)
	fmt.Fscanln(stdin, &a)
	fmt.Fscanln(stdin, &b)

	if a > 0 {
		if b > 0 {
			fmt.Println(1)
		} else {
			fmt.Println(4)
		}
	} else {
		if b > 0 {
			fmt.Println(2)
		} else {
			fmt.Println(3)
		}
	}
}
