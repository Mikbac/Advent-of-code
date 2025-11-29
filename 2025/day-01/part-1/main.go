package main

// Created by MikBac on 2025

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
	sum := len(lines)
	return sum
}
