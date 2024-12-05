package main

// Created by MikBac on 2024

import (
	"fmt"
	"sort"
	"strconv"
	"strings"
	"utils/lineReader"
)

func main() {
	lines := lineReader.ReadStringsFromFile("input")
	answer := solution(lines)

	fmt.Println("Answer:", answer)
}

func solution(lines []string) int {
	listOne := []int{}
	listTwo := []int{}
	for _, line := range lines {
		s1, _ := strconv.Atoi(strings.Split(line, "   ")[0])
		s2, _ := strconv.Atoi(strings.Split(line, "   ")[1])
		listOne = append(listOne, s1)
		listTwo = append(listTwo, s2)
	}

	sort.Sort(sort.IntSlice(listOne))
	sort.Sort(sort.IntSlice(listTwo))

	sum := 0
	for i := 0; i < len(lines); i++ {
		if listOne[i] > listTwo[i] {
			sum += listOne[i] - listTwo[i]
		} else {
			sum += listTwo[i] - listOne[i]
		}
	}

	return sum
}
