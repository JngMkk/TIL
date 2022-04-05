package main

import (
	"fmt"
	"nomadcoder/project1/banking"
)

func main() {
	account := banking.Account{Owner: "eddie", Balance: 1000}
	fmt.Println(account)
}
