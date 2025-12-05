package main

// Created by MikBac on 2025

import (
	"fmt"
	"utils/lineReader"
)

func main() {
	lines := lineReader.ReadStringsFromFile("sample")
	//lines := lineReader.ReadStringsFromFile("input")
	answer := solution(lines)

	fmt.Println("Answer:", answer)
}

func solution(lines []string) int {
	for _, line := range lines {
		fmt.Println(line)
	}

	return len(lines)
}
