package main

import (
	"bufio"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
	"regexp"
	"strings"
	"sync"

	"github.com/fatih/color"
)

func readRegexPatternsFromFile(filePath string) []*regexp.Regexp {
	patterns := []*regexp.Regexp{}
	file, err := os.Open(filePath)
	if err != nil {
		log.Fatalf("Error opening regex patterns file: %v", err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		pattern := strings.TrimSpace(scanner.Text())
		if pattern != "" {
			re := regexp.MustCompile("(?i)" + pattern)
			patterns = append(patterns, re)
		}
	}

	if err := scanner.Err(); err != nil {
		log.Fatalf("Error reading regex patterns file: %v", err)
	}

	return patterns
}

func readBannerFromFile(filePath string) string {
	content, err := ioutil.ReadFile(filePath)
	if err != nil {
		log.Fatalf("Error reading banner file: %v", err)
	}
	return string(content)
}

func searchLeakedCredentials(url string, patterns []*regexp.Regexp, wg *sync.WaitGroup) {
	defer wg.Done()

	response, err := http.Get(url)
	if err != nil {
		log.Printf("Failed to retrieve content from %s: %v", url, err)
		return
	}
	defer response.Body.Close()

	if response.StatusCode != http.StatusOK {
		log.Printf("Failed to retrieve content from %s. Status code: %d", url, response.StatusCode)
		return
	}

	content, err := ioutil.ReadAll(response.Body)
	if err != nil {
		log.Printf("Error reading response body: %v", err)
		return
	}

	for _, pattern := range patterns {
		matches := pattern.FindAllString(string(content), -1)
		if len(matches) > 0 {
			color.Red(fmt.Sprintf("Potential leaked credentials found using pattern '%s' at %s:", pattern.String(), url))
			for _, match := range matches {
				color.Red(fmt.Sprintf("  %s", match))
			}
		}
	}
}

func main() {
	// Load banner from file
	bannerFilePath := "config/banner.txt"
	banner := readBannerFromFile(bannerFilePath)
	if banner != "" {
		color.Green(banner)
	}

	// Load regex patterns from file
	regexPatternsFilePath := "config/regex_patterns.txt"
	patterns := readRegexPatternsFromFile(regexPatternsFilePath)
	if len(patterns) == 0 {
		log.Println("No regex patterns loaded. Exiting.")
		return
	}

	// Parse command-line arguments (URLs to search)
	args := os.Args
	if len(args) < 2 {
		log.Println("Usage: go run main.go <URL1> [<URL2> ...]")
		return
	}
	urls := args[1:]

	// Perform search for leaked credentials concurrently
	var wg sync.WaitGroup
	for _, url := range urls {
		wg.Add(1)
		go searchLeakedCredentials(url, patterns, &wg)
	}

	// Wait for all search goroutines to complete
	wg.Wait()
}
