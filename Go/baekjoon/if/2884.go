package main

import "fmt"

func main() {
	var h, m int
	fmt.Scan(&h, &m)
	if m >= 45 {
		fmt.Printf("%d %d\n", h, m-45)
	} else {
		if h == 0 {
			fmt.Printf("%d %d\n", 23, m+15)
		} else {
			fmt.Printf("%d %d\n", h-1, m+15)
		}
	}
}
