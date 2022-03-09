package main

import (
	"fmt"
	htemplate "html/template" // 별칭
	"math/rand"
	_ "strings" // 빈칸지시자. import 했지만 사용하지는 않겠다. 패키지 초기화에 따른 부가효과를 위해서
	"text/template"
)

func main() {
	fmt.Println(rand.Int())
	template.New("foo").Parse(`{{define "T"}}Hello`)
	htemplate.New("foo").Parse(`{{define "T"}}Hello`)
}
