package main

import "fmt"

// 구조체 선언
// type 타입명 struct {
// 	...
// }

type House struct {
	Address  string
	Size     int
	Price    float64
	Category string
}

func main() {
	// var house House = House{"서울시 강남구", 28, 10, "아파트"}
	var house House
	house.Address = "서울시 강남구"
	house.Size = 28
	house.Price = 10
	house.Category = "아파트"

	fmt.Printf("주소 : %s, 사이즈 : %d평, 가격 : %.2f억원, 종류 : %s \n",
		house.Address,
		house.Size,
		house.Price,
		house.Category)
}
