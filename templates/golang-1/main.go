package main

import (
	"fmt"
	"utils/lineReader"
)

func main() {
	lines := lineReader.ReadFromFile("sample")
	answer := solution(lines)

	fmt.Println("Answer:", answer)
}

func solution(lines []string) int {
	for _, line := range lines {
		fmt.Println(line)
	}

	return len(lines)
}
