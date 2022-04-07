package main

import (
	"errors"
	"fmt"
	"net/http"
)

var errRequestFailed = errors.New("request fail")

func hitURL(url string) error {
	fmt.Println("Checking:", url)
	res, err := http.Get(url)
	if err != nil || res.StatusCode != 200 {
		return errRequestFailed
	}
	return nil
}

func main() {
	results := make(map[string]string)
	urls := []string{
		"https://www.airbnb.com",
		"https://www.google.com",
		"https://amazon.com",
		"https://instagram.com",
	}
	for _, url := range urls {
		result := "OK"
		err := hitURL(url)
		if err != nil {
			result = "FAILED"
		}
		results[url] = result
	}
	for url, result := range results {
		fmt.Println(url, result)
	}
}
