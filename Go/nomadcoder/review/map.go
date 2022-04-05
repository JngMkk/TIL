package main

import "fmt"

func main() {
	mapp := map[string]string{"name": "eddie", "age": "22"}
	for k, v := range mapp {
		fmt.Println(k, v)
	}
}
