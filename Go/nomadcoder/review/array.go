package main

import "fmt"

func main() {
	names := [5]string{"hi", "hello", "bye"}
	// names[3] = "eddie"
	// names[4] = "miffy"
	vars := []string{"hi", "hello", "bye"}
	vars = append(vars, "eddie", "miffy", "jngmk")
	fmt.Println(names, vars)
}
