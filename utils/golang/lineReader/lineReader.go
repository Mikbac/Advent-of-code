package lineReader

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func ReadStringsFromFile(filename string) []string {
	content, err := os.ReadFile(filename)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	lines := strings.Split(string(content), "\r\n")

	// remove last line if blank
	if lines[len(lines)-1] == "" {
		return lines[:len(lines)-1]
	} else {
		return lines
	}
}

func ReadIntsFromFile(filename string) []int {
	content, err := os.ReadFile(filename)
	if err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
	lines := strings.Split(string(content), "\r\n")
	var numbers []int

	// convert only numbers
	for _, v := range lines {
		if v == "" {
			continue
		}
		j, err := strconv.Atoi(v)
		if err != nil {
			panic(err)
		}
		numbers = append(numbers, j)
	}

	return numbers
}
