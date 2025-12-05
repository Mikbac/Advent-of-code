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
			answerCounter += change / 100
			change = change % 100

			current = current + change

			if current > 99 {
				answerCounter++
				current -= 100
			}
		} else {
			answerCounter += change / 100
			change = change % 100

			if current <= change && current != 0 {
				answerCounter++
			}

			current = current - change

			if current < 0 {
				current += 100
			}
		}

	}

	return answerCounter
}
