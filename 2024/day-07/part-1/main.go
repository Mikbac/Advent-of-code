package main

// Created by MikBac on 2024

import (
	"fmt"
	"strconv"
	"strings"
	"utils/combinatorics"
	"utils/lineReader"
)

func main() {
	//lines := lineReader.ReadStringsFromFile("sample")
	lines := lineReader.ReadStringsFromFile("input")
	answer := solution(lines)

	fmt.Println("Answer:", answer)
}

func solution(lines []string) int {
	sum := 0
	for _, line := range lines {
		v := strings.Split(line, ": ")
		exp, _ := strconv.Atoi(v[0])
		var numb []int
		for _, n := range strings.Split(v[1], " ") {
			nn, _ := strconv.Atoi(n)
			numb = append(numb, nn)
		}
		sum += evaluate(exp, numb)
	}

	return sum
}

func evaluate(ex int, numbers []int) int {
	sum := 0
	for _, c := range combinatorics.VariationsWithRepetition([]string{"+", "*"}, len(numbers)-1, []string{}) {
		res := numbers[0]
		for i := 1; i < len(numbers); i++ {
			if c[i-1] == "+" {
				res = res + numbers[i]
			} else if c[i-1] == "*" {
				res = res * numbers[i]
			}
		}
		if res == ex {
			sum += ex
			break
		}
	}

	return sum
}
