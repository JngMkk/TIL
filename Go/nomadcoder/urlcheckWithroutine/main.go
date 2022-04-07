package main

import (
	"fmt"
	"net/http"
)

type result struct {
	url    string
	status string
}

func hitURL(url string, c chan<- result) {
	res, err := http.Get(url)
	status := "OK"

	if err != nil || res.StatusCode != 200 {
		status = "FAILED"
	}

	c <- result{url: url, status: status}
}

func main() {
	results := make(map[string]string)
	c := make(chan result)
	urls := []string{
		"https://www.airbnb.com",
		"https://www.google.com",
		"https://amazon.com",
		"https://instagram.com",
	}

	for _, url := range urls {
		go hitURL(url, c)
	}

	for range urls {
		res := <-c
		results[res.url] = res.status
	}

	for url, status := range results {
		fmt.Println(url, status)
	}
}
