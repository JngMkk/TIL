package scrapper

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

// job struct
type extractedJob struct {
	jobURL   string
	title    string
	location string
	salary   string
	summary  string
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

// return clean string
func CleanString(str string) string {
	return strings.Join(strings.Fields(strings.TrimSpace(str)), " ")
}

// total page counts
func getPages(url string) int {
	pages := 0
	res, err := http.Get(url)
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

// hit page
func getPage(page int, url string, mainC chan<- []extractedJob) {
	var jobs []extractedJob
	c := make(chan extractedJob)

	pageURL := url + "start=" + strconv.Itoa(page*50)
	fmt.Println("Requesting", pageURL)
	res, err := http.Get(pageURL)
	checkErr(err)
	checkCode(res)

	defer res.Body.Close()

	doc, err := goquery.NewDocumentFromReader(res.Body)
	checkErr(err)

	searchCards := doc.Find(".tapItem.fs-unmask")
	searchCards.Each(func(i int, card *goquery.Selection) {
		go extratJob(card, c)
	})

	for i := 0; i < searchCards.Length(); i++ {
		job := <-c
		jobs = append(jobs, job)
	}

	mainC <- jobs
}

// into struct
func extratJob(card *goquery.Selection, c chan<- extractedJob) {
	var link string
	href, _ := card.Attr("data-jk")
	link = "https://kr.indeed.com/viewjob?jk=" + href
	title := CleanString(card.Find(".jobTitle > span").Text() + " " + card.Find(".companyName").Text())
	location := CleanString(card.Find(".companyLocation").Text())
	salary := CleanString(card.Find(".attribute_snippet").Text())
	summary := CleanString(card.Find(".job-snippet").Text())

	c <- extractedJob{
		jobURL:   link,
		title:    title,
		location: location,
		salary:   salary,
		summary:  summary,
	}
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

func Scrape(term string) {
	var baseURL string = "https://kr.indeed.com/jobs?q=" + term + "&limit=50&"
	var jobs []extractedJob
	c := make(chan []extractedJob)

	totalPages := getPages(baseURL)
	for i := 0; i < totalPages; i++ {
		go getPage(i, baseURL, c)
	}

	for i := 0; i < totalPages; i++ {
		extractedJob := <-c
		jobs = append(jobs, extractedJob...)
	}

	writeJobs(jobs)
	fmt.Println("Done!", len(jobs))
}
