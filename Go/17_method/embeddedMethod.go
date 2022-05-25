package main

import "fmt"

type User struct {
	Name string
	Age  int
}

func (u User) String() string {
	return fmt.Sprintf("%s, %d", u.Name, u.Age)
}

type VIPUser struct {
	User     // embedded field
	VIPLevel int
}

func (v VIPUser) VipLevel() int {
	return v.VIPLevel
}

// func (v VIPUser) String() string {
// 	return fmt.Sprintf("%d", v.VIPLevel)
// }

func main() {
	vip := VIPUser{User{"Hwarang", 34}, 5}
	// 상속은 아님 단순히 포함..
	fmt.Println(vip.String())
}
