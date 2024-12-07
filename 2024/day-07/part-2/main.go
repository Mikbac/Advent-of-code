package main

// Created by MikBac on 2024

import (
	"fmt"
	"strconv"
	"strings"
	"utils/lineReader"
)

func main() {
	lines := lineReader.ReadStringsFromFile("sample")
	//lines := lineReader.ReadStringsFromFile("input")
	answer := solution(lines)

	fmt.Println("Answer:", answer)
}

func solution(lines []string) int {
	sum := 0
	for _, line := range lines {
		v := strings.Split(line, ": ")
		exp, _ := strconv.Atoi(v[0])
		numb := []int{}
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
	for _, c := range generateCombination([]string{"+", "*"}, len(numbers)-1, []string{}) {
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

func generateCombination(input []string, depth int, product []string) [][]string {
	if depth == len(product) {
		tmp := make([]string, len(product))
		copy(tmp, product)
		return [][]string{tmp}
	} else {
		p1 := generateCombination(input, depth, append(product, "+"))
		p2 := generateCombination(input, depth, append(product, "*"))
		p3 := generateCombination(input, depth, append(product, "||"))
		return append(append(p1, p2...), p3...)
	}
}
