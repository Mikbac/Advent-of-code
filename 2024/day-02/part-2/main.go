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
	totalSafeCounter := 0
	for _, line := range lines {
		totalSafeCounter += 1
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
				success := false
				for j := 0; j < len(codes); j++ {
					if nextRound(RemoveIndex(codes, j)) {
						success = true
						break
					}
				}
				if !success {
					totalSafeCounter -= 1
				}
				break
			}
		}

	}

	return totalSafeCounter
}

func nextRound(s string) bool {
	status := true
	codes := strings.Split(s, " ")
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
			status = false
			break
		}
	}
	return status
}

func RemoveIndex(s []string, index int) string {
	tmp := make([]string, len(s))
	copy(tmp, s)
	return strings.Join(append(tmp[:index], tmp[index+1:]...), " ")
}
