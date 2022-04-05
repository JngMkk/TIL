package main

import "fmt"

type person struct {
	name    string
	age     int
	favFood []string
}

func main() {
	favFood := []string{"kimchi", "ramen"}
	per := person{"eddie", 19, favFood}
	per2 := person{name: "miffy", age: 22, favFood: favFood}
	fmt.Println(per, per.name)
	fmt.Println(per2, per2.age)
}
