package main

import (
	"fmt"
	"nomadcoder/accounts/accounts"
)

func main() {
	account := accounts.NewAccount("eddie")
	account.Deposit(2000)
	err := account.Withdraw(3000)
	if err != nil {
		// log.Fatalln(err) -> 프로그램 종료
		fmt.Println(err)
	}
	fmt.Println(account)
}
