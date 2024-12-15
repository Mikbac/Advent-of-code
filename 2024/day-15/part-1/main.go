package main

// Created by MikBac on 2024

import (
	"fmt"
	"strings"
	"utils/lineReader"
)

func main() {
	//lines := lineReader.ReadStringsFromFile("sample1")
	//lines := lineReader.ReadStringsFromFile("sample2")
	lines := lineReader.ReadStringsFromFile("input")
	answer := solution(lines)

	fmt.Println("Answer:", answer)
}

func solution(lines []string) int {
	var wMap [][]string
	ins := ""
	rL := position{}
	isMap := true
	for i, line := range lines {
		if line == "" {
			isMap = false
			continue
		}
		if isMap {
			wMap = append(wMap, strings.Split(line, ""))
			if strings.Contains(line, "@") {
				y := strings.Index(line, "@")
				rL = position{i, y}
				wMap[i][y] = "."
			}
		}
		if !isMap {
			ins += line
		}

	}

	for _, c := range ins {
		rL, wMap = makeStep(string(c), wMap, rL)
	}

	sum := 0
	for i, _ := range wMap {
		for j, _ := range wMap[i] {
			if wMap[i][j] == "O" {
				sum += 100*i + j
			}
		}
	}

	return sum
}

func makeStep(c string, wMap [][]string, rL position) (position, [][]string) {
	var ia bool
	var nRL position
	var nWM [][]string
	if c == ">" {
		ia, nWM = isStepAvailable(vector{0, 1}, wMap, position{rL.x, rL.y + 1})
		if ia {
			nRL = position{rL.x, rL.y + 1}
		}
	} else if c == "v" {
		ia, nWM = isStepAvailable(vector{1, 0}, wMap, position{rL.x + 1, rL.y})
		if ia {
			nRL = position{rL.x + 1, rL.y}
		}
	} else if c == "<" {
		ia, nWM = isStepAvailable(vector{0, -1}, wMap, position{rL.x, rL.y - 1})
		if ia {
			nRL = position{rL.x, rL.y - 1}
		}
	} else if c == "^" {
		ia, nWM = isStepAvailable(vector{-1, 0}, wMap, position{rL.x - 1, rL.y})
		if ia {
			nRL = position{rL.x - 1, rL.y}
		}
	}

	if ia {
		return nRL, nWM
	} else {
		return rL, wMap
	}
}

func isStepAvailable(v vector, wMap [][]string, nP position) (bool, [][]string) {
	if wMap[nP.x][nP.y] == "#" {
		return false, wMap
	} else if wMap[nP.x][nP.y] == "." {
		return true, wMap
	} else {
		return pushBox(v, wMap, nP)
	}
}

func pushBox(v vector, wMap [][]string, nP position) (bool, [][]string) {
	if wMap[nP.x+v.x][nP.y+v.y] == "O" {
		isP, nWM := pushBox(v, wMap, position{nP.x + v.x, nP.y + v.y})
		if isP {
			wMap[nP.x][nP.y] = "."
			wMap[nP.x+v.x][nP.y+v.y] = "O"
		}
		return isP, nWM
	} else if wMap[nP.x+v.x][nP.y+v.y] == "." {
		wMap[nP.x][nP.y] = "."
		wMap[nP.x+v.x][nP.y+v.y] = "O"
		return true, wMap
	} else {
		return false, wMap
	}

}

type position struct {
	x int
	y int
}

type vector struct {
	x int
	y int
}
