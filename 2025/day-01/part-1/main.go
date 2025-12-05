package main

// Created by MikBac on 2025

import (
	"fmt"
	"strconv"
	"utils/lineReader"
)

func main() {
	//lines := lineReader.ReadStringsFromFile("sample")
	lines := lineReader.ReadStringsFromFile("input")
	answer := solution(lines)

	fmt.Println("Answer:", answer)
}

func solution(lines []string) int {
	answerCounter := 0
	current := 50

	for _, line := range lines {
		rot := string(line[0])
		numPart := line[1:]
		change, _ := strconv.Atoi(numPart)

		if rot == "R" {
			current = (current + change) % 100
		} else {
			current = (current - change) % 100
			if current < 0 {
				current = 100 + current
			}
		}

		if current == 0 {
			answerCounter++
		}

	}

	return answerCounter
}
