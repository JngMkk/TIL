package main

import "fmt"

// go는 생성자, 소멸자 x
type account struct {
	balance   int
	firstname string
	lastname  string
}

func (a1 *account) withdrawPointer(amount int) {
	a1.balance -= amount
}

// 얘는 안나옴
func (a2 account) withdrawValue(amount int) {
	a2.balance -= amount
}

func (a2 account) withdrawValue2(amount int) account {
	a2.balance -= amount
	return a2
}

func main() {
	var mainA *account = &account{100, "joe", "park"}
	mainA.withdrawPointer(30)
	fmt.Println(mainA.balance)

	// 값으로 반환받지 않음
	mainA.withdrawValue(20)
	fmt.Println(mainA.balance)

	*mainA = mainA.withdrawValue2(20)
	fmt.Println(mainA.balance)
}
