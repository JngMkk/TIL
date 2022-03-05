package main

import (
	"fmt"
	"time"
)

// 무한 루프
func main() {
	i := 1
	for { // for true랑 같음
		time.Sleep(time.Second) // 1초 sleep
		fmt.Println(i)
		i++
	}
}
