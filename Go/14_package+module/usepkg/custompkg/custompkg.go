package custompkg

import "fmt"

type Student struct { // 대문자 -> 외부 공개
	Name  string
	Age   int
	score int // 필드 소문자 -> 외부 공개 x
}

var Ratio int // 대문자 -> 외부 공개
var ttt int   // 소문자 -> 외부 공개 x

const PI = 3.14
const pi2 = 3.1415

func PrintCustom() {
	fmt.Println("This is custom package!")
}

func printcustom2() { // 소문자로 쓰면 외부로 공개되지 않음
	fmt.Println("This is custom package!")
}
