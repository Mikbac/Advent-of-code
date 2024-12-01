package main

import (
	"fmt"
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

	mapQ := make(map[int]int)
	for _, i := range listTwo {
		mapQ[i] = mapQ[i] + 1
	}

	sum := 0
	for _, i := range listOne {
		sum += i * mapQ[i]
	}

	return sum
}
