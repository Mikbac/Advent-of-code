package main

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
	safeCounter := 0
	for _, line := range lines {
		safeCounter += 1
		codes := strings.Split(line, " ")
		previousCode, _ := strconv.Atoi(codes[0])
		tend := ""
		for i := 1; i < len(codes); i++ {
			currentCode, _ := strconv.Atoi(codes[i])
			dif := currentCode - previousCode
			if tend == "" && dif <= 3 && dif >= -3 && dif != 0 {
				if dif > 0 {
					tend = "+"
				} else {
					tend = "-"
				}
				previousCode = currentCode
			} else if (tend == "+" && dif <= 3 && dif > 0) || (tend == "-" && dif >= -3 && dif < 0) {
				previousCode = currentCode
			} else {
				safeCounter -= 1
				break
			}
		}

	}

	return safeCounter
}
