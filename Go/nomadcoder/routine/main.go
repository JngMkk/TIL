package main

import (
	"fmt"
	"time"
)

func count(person string) {
	for i := 0; i < 10; i++ {
		fmt.Println(person, "hello", i)
		time.Sleep(time.Second)
	}
}

func main() {
	go count("eddie")
	count("miffy")
}
