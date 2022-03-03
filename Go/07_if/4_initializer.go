package main

import "fmt"

func UploadFile() (string, bool) {
	return "go", true
}

func main() {
	// if 초기문; 조건문 {
	// 	 문장
	// }
	// 성공여부 검사할 때 사용

	if filename, success := UploadFile(); success {
		fmt.Println("Upload success", filename)
	} else {
		fmt.Println("Failed to upload")
	}
}
