package main

import (
	"fmt"
	"time"
)

func hello(person string, c chan string) {
	time.Sleep(time.Second * 5)
	fmt.Println(person)
	c <- person + " hello"
}

func main() {
	c := make(chan string)
	people := [2]string{"eddie", "miffy"}
	for _, person := range people {
		go hello(person, c)
	}
	for range people {
		fmt.Println(<-c)
	}
}
