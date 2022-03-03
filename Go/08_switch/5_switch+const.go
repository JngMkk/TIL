package main

import "fmt"

type ColorType int // 별칭 타입

const (
	Red    ColorType = iota // 0
	Blue                    // 1
	Green                   // 2
	Yellow                  // 3
)

func colorToString(color ColorType) string {
	switch color {

	case Red:
		return "Red"

	case Blue:
		return "Blue"

	case Green:
		return "Green"

	case Yellow:
		return "Yellow"

	default:
		return "Undefined"
	}
}

func getMyFavoriteColor() ColorType {
	return Red
}

func main() {
	fmt.Println("My favorite color is", colorToString(getMyFavoriteColor()))
	fmt.Println("hate color is", colorToString(1))
}
