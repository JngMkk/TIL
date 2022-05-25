package main

import "fmt"

// 패키지 내의 지역타입만 메서드 정의 가능
type account struct {
	balance int
}

func withdrawFunc(a *account, amount int) {
	a.balance -= amount
}

func (a *account) withdrawMethod(amount int) {
	a.balance -= amount
}

func main() {
	a := &account{100} // *account

	withdrawFunc(a, 30)

	a.withdrawMethod(30)

	fmt.Printf("%d\n", a.balance)
}
