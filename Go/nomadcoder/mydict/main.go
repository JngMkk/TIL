package main

import (
	"fmt"
	"nomadcoder/mydict/mydict"
)

func main() {
	dictionary := mydict.Dictionary{}
	dictionary["first"] = "first word"
	fmt.Println(dictionary["first"])

	def, err := dictionary.Search("second")
	if err != nil {
		fmt.Println(err)
	} else {
		fmt.Println(def)
	}

	err2 := dictionary.Add("first", "fi word")
	if err2 != nil {
		fmt.Println(err2)
	}

	first, _ := dictionary.Search("first")
	fmt.Println(first)

	err3 := dictionary.Update("first", "hello")
	if err3 != nil {
		fmt.Println(err3)
	}

	fmt.Println(dictionary["first"])

	err4 := dictionary.Update("second", "hi")
	if err4 != nil {
		fmt.Println(err4)
	}

	err5 := dictionary.Add("second", "hi")
	if err5 != nil {
		fmt.Println(err5)
	}
	fmt.Println(dictionary)

	err6 := dictionary.Delete("second")
	if err6 != nil {
		fmt.Println(err6)
	}
	fmt.Println(dictionary)
}
