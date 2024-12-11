package main

// Created by MikBac on 2024

import (
	"fmt"
	"strconv"
	"strings"
	"utils/lineReader"
)

func main() {
	//lines := lineReader.ReadStringsFromFile("sample1")
	//lines := lineReader.ReadStringsFromFile("sample2")
	lines := lineReader.ReadStringsFromFile("input")
	answer := solution(lines[0])

	fmt.Println("Answer:", answer)
}

func solution(line string) int {
	var stones []int
	for _, c := range strings.Split(line, " ") {
		n, _ := strconv.Atoi(c)
		stones = append(stones, n)
	}

	for i := 0; i < 25; i++ {
		stones = updateStones(stones)
	}

	return len(stones)
}

func updateStones(stones []int) []int {
	for i := 0; i < len(stones); i++ {
		if stones[i] == 0 {
			stones[i] = 1
		} else if len(strconv.Itoa(stones[i]))%2 == 0 {
			s := strconv.Itoa(stones[i])
			n1, _ := strconv.Atoi(s[:len(s)/2])
			n2, _ := strconv.Atoi(s[len(s)/2:])
			stones[i] = n2
			stones = append(stones[:i], append([]int{n1}, stones[i:]...)...)
			i++
		} else {
			stones[i] = stones[i] * 2024
		}
	}
	return stones
}
