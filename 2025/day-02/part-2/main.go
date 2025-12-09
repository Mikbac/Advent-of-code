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
	answer := solution(lines[0])

	fmt.Println("Answer:", answer)
}

func solution(lines string) int {
	ranges := strings.Split(lines, ",")
	respSum := 0
	for _, rang := range ranges {
		startS := strings.Split(rang, "-")[0]
		startN, _ := strconv.Atoi(strings.Split(rang, "-")[0])
		endN, _ := strconv.Atoi(strings.Split(rang, "-")[1])

		visited := make(map[int]bool)

		for startN <= endN {

			for i := 1; i <= len(startS)/2; i++ {

				currentStage := ""
				currentStage = startS[:i]

				n, _ := strconv.Atoi(strings.Repeat(currentStage, (len(startS) / i)))

				if n > endN {
					continue
				}

				if n >= startN && n <= endN && !visited[n] {
					respSum += n
					visited[n] = true
				}

			}

			startN++
			startS = strconv.Itoa(startN)
		}
	}

	return respSum
}
