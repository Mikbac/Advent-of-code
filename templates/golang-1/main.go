package main

// Created by MikBac on 2024

import (
	"fmt"
	"utils/lineReader"
)

func main() {
	lines := lineReader.ReadStringsFromFile("sample")
	answer := solution(lines)

	fmt.Println("Answer:", answer)
}

func solution(lines []string) int {
	for _, line := range lines {
		fmt.Println(line)
	}

	return len(lines)
}
