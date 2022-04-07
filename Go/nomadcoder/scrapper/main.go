package main

import (
	"nomadcoder/scrapper/scrapper"
	"os"
	"strconv"
	"strings"
	"time"

	"github.com/labstack/echo"
)

const fileName string = "jobs.csv"

func handleHome(c echo.Context) error {
	return c.File("home.html")
}

func handleScrap(c echo.Context) error {
	defer os.Remove(fileName)
	now := time.Now()
	current := now.Month().String() + "-" + strconv.Itoa(now.Day())
	term := strings.ToLower(scrapper.CleanString(c.FormValue("term")))
	scrapper.Scrape(term)
	return c.Attachment(fileName, current+" "+term+"jobs.csv")
}

func main() {
	e := echo.New()
	e.GET("/", handleHome)
	e.POST("/scrap", handleScrap)
	e.Logger.Fatal(e.Start(":1323"))
}
