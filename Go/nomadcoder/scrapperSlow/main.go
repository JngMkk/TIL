package main

import (
	"encoding/csv"
	"fmt"
	"log"
	"net/http"
	"os"
	"strconv"
	"strings"

	"github.com/PuerkitoBio/goquery"
)

var jobURL string
var baseURL string = "https://kr.indeed.com/jobs?q=python&limit=50&"

// job struct
type extractedJob struct {
	jobURL   string
	title    string
	location string
	salary   string
	summary  string
}

// total page counts
func getPages() int {
	pages := 0
	res, err := http.Get(baseURL)
	checkErr(err)
	checkCode(res)

	defer res.Body.Close()

	doc, err := goquery.NewDocumentFromReader(res.Body)
	checkErr(err)

	doc.Find(".pagination").Each(func(i int, s *goquery.Selection) {
		pages = s.Find("a").Length()
	})
	return pages
}

// check error
func checkErr(err error) {
	if err != nil {
		log.Fatalln(err)
	}
}

// check statuscode
func checkCode(res *http.Response) {
	if res.StatusCode != 200 {
		log.Fatalln("Request failed with Status:", res.StatusCode)
	}
}

// hit page
func getPage(page int) []extractedJob {
	var jobs []extractedJob
	pageURL := baseURL + "start=" + strconv.Itoa(page*50)
	fmt.Println("Requesting", pageURL)
	res, err := http.Get(pageURL)
	checkErr(err)
	checkCode(res)

	defer res.Body.Close()

	doc, err := goquery.NewDocumentFromReader(res.Body)
	checkErr(err)

	searchCards := doc.Find(".tapItem.fs-unmask")
	searchCards.Each(func(i int, card *goquery.Selection) {
		job := extratJob(card)
		jobs = append(jobs, job)
	})
	return jobs
}

// into struct
func extratJob(card *goquery.Selection) extractedJob {
	href, _ := card.Attr("data-jk")
	jobURL = "https://kr.indeed.com/viewjob?jk=" + href
	title := cleanString(card.Find(".jobTitle > span").Text() + " " + card.Find(".companyName").Text())
	location := cleanString(card.Find(".companyLocation").Text())
	salary := cleanString(card.Find(".attribute_snippet").Text())
	summary := cleanString(card.Find(".job-snippet").Text())
	return extractedJob{
		jobURL:   jobURL,
		title:    title,
		location: location,
		salary:   salary,
		summary:  summary,
	}
}

// return clean string
func cleanString(str string) string {
	return strings.Join(strings.Fields(strings.TrimSpace(str)), " ")
}

// to csv
func writeJobs(jobs []extractedJob) {
	file, err := os.Create("jobs.csv")
	checkErr(err)

	w := csv.NewWriter(file)

	defer w.Flush()

	headers := []string{"jobURL", "Title", "Location", "Salary", "Summary"}
	wErr := w.Write(headers)
	checkErr(wErr)

	for _, job := range jobs {
		jobSlice := []string{job.jobURL, job.title, job.location, job.salary, job.summary}
		jwErr := w.Write(jobSlice)
		checkErr(jwErr)
	}
}

func main() {
	var jobs []extractedJob
	totalPages := getPages()
	for i := 0; i < totalPages; i++ {
		extractedJobs := getPage(i)
		jobs = append(jobs, extractedJobs...)
	}
	writeJobs(jobs)
	fmt.Println("Done!", len(jobs))
}
