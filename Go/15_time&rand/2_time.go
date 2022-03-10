package main

import (
	"fmt"
	"time"
)

func main() {
	loc, _ := time.LoadLocation("Asia/Seoul")
	const longForm = "Jan 2, 2006 at 3:04pm"
	t1, _ := time.ParseInLocation(longForm, "Jun 10, 2021 at 10:00pm", loc)
	fmt.Println(t1, t1.Location(), t1.UTC())

	const shortForm = "2006-Jan-02"
	t2, _ := time.Parse(shortForm, "2021-Jun-14")
	fmt.Println(t2, t2.Location())

	t3, err := time.Parse("2021-06-21 15:20:21", "2021-06-14 20:04:05")
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println(t3, t3.Location())

	d := t2.Sub(t1)
	fmt.Println(d)
}
