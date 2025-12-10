package main

// Created by MikBac on 2025

import (
	"fmt"
	"strconv"
	"strings"
	"utils/lineReader"
)

func main() {
	//lines := lineReader.ReadStringsFromFile("sample")
	lines := lineReader.ReadStringsFromFile("input")
	answer := solution(lines)

	fmt.Println("Answer:", answer)
}

func solution(lines []string) int {
	result := 0
	for _, line := range lines {
		numbs := strings.Split(line, "")
		maxNumbOne, _ := strconv.Atoi(numbs[0])
		maxNumbOnePos := -1

		maxNumbTwo, _ := strconv.Atoi(numbs[len(numbs)-1])

		for p, n := range numbs[1 : len(numbs)-1] {
			nextNumber, _ := strconv.Atoi(n)

			if nextNumber > maxNumbOne {
				maxNumbOne = nextNumber
				maxNumbOnePos = p
			}

		}

		for p, n := range numbs[1:] {
			nextNumber, _ := strconv.Atoi(n)

			if nextNumber > maxNumbTwo && p > maxNumbOnePos {
				maxNumbTwo = nextNumber
			}

		}

		sum, _ := strconv.Atoi(strconv.Itoa(maxNumbOne) + strconv.Itoa(maxNumbTwo))
		result += sum
	}

	return result
}
