package main

import "fmt"

type Data struct {
	value int
	data  [200]int
}

func ChangeData(arg Data) {
	arg.value = 999
	arg.data[100] = 999
}

func ChangeData2(arg *Data) {
	arg.value = 999
	arg.data[100] = 999
	// (*arg).value = 999
	// (*arg).data[100] = 999
}

func main() {

	var data Data
	var p *Data = &Data{}
	// new() 내장함수 기본값 초기화
	var p2 = new(Data)

	ChangeData(data)
	// 다른 메모리 공간
	fmt.Printf("value = %d\n", data.value)
	fmt.Printf("data[100] = %d\n", data.data[100])

	ChangeData2(&data)
	// 같은 메모리 공간 가리킴
	// 주소값만 복사 (8byte) 성능..
	fmt.Printf("value = %d\n", data.value)
	fmt.Printf("data[100] = %d\n", data.data[100])

	(*p).value = 100
	(*p).data[100] = 777
	fmt.Printf("value = %d\n", (*p).value)
	fmt.Printf("data[100] = %d\n", (*p).data[100])

	(*p2).value = 200
	(*p2).data[100] = 300
	fmt.Printf("value = %d\n", (*p2).value)
	fmt.Printf("data[100] = %d\n", (*p2).data[100])

}
