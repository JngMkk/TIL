package main

import "fmt"

type User struct {
	Name string
	Age  int
}

func NewUser(name string, age int) *User {
	var u = User{name, age}
	return &u
	// stack에 저장하면 func 끝날 때 pointer u가 사라짐
}

func main() {
	// Go에서 탈출 분석하여
	// return 값이 탈출하는 경우 heap에 저장
	userPointer := NewUser("AAA", 23)

	fmt.Println(userPointer)
}
