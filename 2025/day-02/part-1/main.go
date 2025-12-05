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

		midLen := len(startS) / 2

		currentStage := ""
		currentStage = startS[:midLen]
		for {
			n, _ := strconv.Atoi(currentStage + currentStage)

			if n > endN {
				break
			}

			if n >= startN && n <= endN {
				respSum += n
			}

			nexVal, _ := strconv.Atoi(currentStage)
			currentStage = strconv.Itoa(nexVal + 1)
		}
	}

	return respSum
}
