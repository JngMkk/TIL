package main

import "fmt"

type User struct {
	Name string
	ID   string
	Age  int
}

type VIPUser struct {
	User     // 내장된 필드
	VIPLevel int
	Price    int
	Name     string // 필드명이 겹칠 때 우선 순위 높음
}

func main() {
	user := User{"송하나", "hana", 23}
	vip := VIPUser{
		User{"화랑", "hwarang", 48},
		3,
		250,
		"홍길동",
	}

	fmt.Printf("유저 : %s, ID : %s, 나이 : %d\n", user.Name, user.ID, user.Age)
	fmt.Printf("VIP 유저 : %s, ID : %s, 나이 : %d, VIP 레벨 : %d, VIP 가격 : %d만원, VIP 유저 별칭 : %s\n",
		vip.Name,
		vip.ID,
		vip.Age,
		vip.VIPLevel,
		vip.Price,
		vip.User.Name,
	)
}
