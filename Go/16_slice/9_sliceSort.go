package main

import (
	"fmt"
	"sort"
)

type Student struct {
	Name string
	Age  int
}

type Students []Student

func (s Students) Len() int {
	return len(s)
}

func (s Students) Less(i, j int) bool {
	return s[i].Age < s[j].Age
}

func (s Students) Swap(i, j int) {
	s[i], s[j] = s[j], s[i]
}

func main() {
	slice := []int{5, 2, 6, 3, 1, 4}
	sort.Ints(slice)
	fmt.Println(slice)

	s := []Student{
		{"윤", 52},
		{"랑", 33},
		{"류", 22},
		{"하", 18},
	}
	sort.Sort(Students(s))
	fmt.Println(s)
}
