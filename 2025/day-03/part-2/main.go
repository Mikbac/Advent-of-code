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

		topNums := []number{}
		for i, v := range numbs[len(numbs)-12:] {
			n, _ := strconv.Atoi(v)
			topNums = append(topNums, number{n, len(numbs) - 12 + i})
		}

		startPos := 0
		for tnp, _ := range topNums {

			if tnp != 0 {
				startPos = topNums[tnp-1].local + 1
			}

			for p, n := range numbs[startPos:] {
				nextNumber, _ := strconv.Atoi(n)

				if tnp != 11 && topNums[tnp+1].local == p+startPos {
					break
				}

				if (nextNumber > topNums[tnp].value) || (nextNumber == topNums[tnp].value && p+startPos < topNums[tnp].local) {
					topNums[tnp] = number{nextNumber, p + startPos}
				}

			}

		}

		resNum := ""
		for _, tn := range topNums {
			resNum += strconv.Itoa(tn.value)
		}

		sum, _ := strconv.Atoi(resNum)
		result += sum
	}

	return result
}

type number struct {
	value int
	local int
}
