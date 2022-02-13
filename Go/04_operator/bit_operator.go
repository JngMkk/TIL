package main

import "fmt"

func main() {
	var x int8 = 4
	var y int8 = 64

	fmt.Printf("x: %08b x<<2: %08b x<<2: %d\n", x, x<<2, x<<2)
	fmt.Printf("y: %08b y<<2: %08b y<<2: %d\n", y, y<<2, y<<2)

	var z int8 = 10
	fmt.Printf("z: %08b z>>2: %08b z>>2: %d\n", z, z>>2, z>>2)

	var a int8 = 16
	var b int8 = -128
	var c int8 = -1
	var d uint8 = 128
	fmt.Printf("a: %08b a>>2: %08b a>>2: %d\n", a, a>>2, a>>2)
	fmt.Printf("b: %08b b>>2: %08b b>>2: %d\n", uint8(b), uint8(b>>2), b>>2)
	fmt.Printf("c: %08b c>>2: %08b c>>2: %d\n", uint8(c), uint8(c>>2), c>>2) // 음수는 1채워짐 양수는 0채워짐
	fmt.Printf("d: %08b d>>2: %08b d>>2: %d\n", d, d>>2, d>>2)

}
