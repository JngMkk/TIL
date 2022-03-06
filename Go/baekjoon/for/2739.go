package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var a int
	stdin := bufio.NewReader(os.Stdin)
	fmt.Fscanln(stdin, &a)
	for i := 1; i < 10; i++ {
		fmt.Printf("%d * %d = %d", a, i, a*i)
		fmt.Println()
	}
}
