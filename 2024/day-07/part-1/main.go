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

	fmt.Println(generateOptions([]string{"+", "*"}, len(numbers)-1, []string{}))

	return 0
}

func generateOptions(input []string, depth int, product []string) []string {
	if depth == len(product) {
		fmt.Println(product)
		return product
	} else {
		generateOptions(input, depth, append(product, "+"))
		generateOptions(input, depth, append(product, "*"))
	}

	return nil
}
