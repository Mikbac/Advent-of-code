package main

import (
	"fmt"
	"regexp"
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
	var re = regexp.MustCompile(`(mul\([0-9]{0,3},[0-9]{0,3}\))|(do\(\))|(don't\(\))`)
	sum := 0
	do := true
	for _, line := range lines {
		commands := re.FindAllStringSubmatch(line, -1)
		for _, com := range commands {
			if strings.Contains(com[0], "don't") {
				do = false
			} else if strings.Contains(com[0], "do") {
				do = true
			} else if do {
				r := strings.Split(com[0], ",")
				rr1, _ := strconv.Atoi(strings.Replace(r[0], "mul(", "", 1))
				rr2, _ := strconv.Atoi(strings.Replace(r[1], ")", "", 1))
				sum += rr1 * rr2
			}
		}
	}

	return sum
}
