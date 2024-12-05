package main

// Created by MikBac on 2024

import (
	"fmt"
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
	for i := 0; i < len(lines); i++ {
		for j := 0; j < len(lines[i]); j++ {
			if string(lines[i][j]) == "A" {
				check := 0
				check += goDeep(i+2, j-2, -1, 1, []string{"M", "A", "S"}, lines)
				check += goDeep(i-2, j-2, 1, 1, []string{"M", "A", "S"}, lines)
				check += goDeep(i-2, j+2, 1, -1, []string{"M", "A", "S"}, lines)
				check += goDeep(i+2, j+2, -1, -1, []string{"M", "A", "S"}, lines)
				if check == 2 {
					sum++
				}
			}
		}
	}
	return sum
}

func goDeep(i int, j int, iv int, jv int, nl []string, l []string) int {
	if len(nl) == 0 {
		return 1
	}

	c, n := nl[0], nl[1:]

	if isCorrect(i+iv, len(l), j+jv, len(l[0])) && string(l[i+iv][j+jv]) == c {
		return goDeep(i+iv, j+jv, iv, jv, n, l)
	} else {
		return 0
	}

}

func isCorrect(i int, il int, j int, jl int) bool {
	if i < 0 || j < 0 || i > il-1 || j > jl-1 {
		return false
	}
	return true
}
