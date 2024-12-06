package main

// Created by MikBac on 2024

import (
	"fmt"
	"slices"
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
	rules := make(map[string][]string)
	sum := 0
	ip := false
	for _, line := range lines {
		if len(line) == 0 {
			ip = true
		}
		if !ip {
			r := strings.Split(line, "|")
			r1 := r[0]
			r2 := r[1]
			rules[r1] = append(rules[r1], r2)
		} else {
			pages := strings.Split(line, ",")
			broken := false
			for i, p := range pages {
				cp := pages[:i]
				for _, pp := range cp {
					if slices.Contains(rules[p], pp) {
						broken = true
					}
				}
			}
			if broken {

				b := true
				for b {
					b = false
					for i, p := range pages {
						cp := pages[:i]
						for ii, pp := range cp {
							if slices.Contains(rules[p], pp) {
								b = true
								pages[ii], pages[i] = pages[i], pages[ii]
							}
						}

					}
				}

				v, _ := strconv.Atoi(pages[len(pages)/2])
				sum += v
			}

		}
	}

	return sum
}
