package main

// Created by MikBac on 2024

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
	ans := 0
	for i := 0; i < len(lines); i += 4 {

		bA := extractButton(lines[i])
		bB := extractButton(lines[i+1])
		eX, eY := extractPrize(lines[i+2])

		ans += findOptimal(bA, bB, eX+10000000000000, eY+10000000000000)
	}

	return ans
}

func findOptimal(bA button, bB button, eX int, eY int) int {
	// System of two equations
	// e.g.
	// x * 26 + y * 67 = 12748
	// x * 66 + y * 21 = 12176
	// https://www.wolframalpha.com/input?i=Assuming+a+system+of+two+equations&assumption=%7B%22F%22%2C+%22SolveSystemOf2EquationsCalculator%22%2C+%22equation1%22%7D+-%3E%22x*26%2By*67%3D12748%22&assumption=%7B%22F%22%2C+%22SolveSystemOf2EquationsCalculator%22%2C+%22equation2%22%7D+-%3E%22x*66%2By*21%3D12176%22

	det := float64(bA.x)*float64(bB.y) - float64(bA.y)*float64(bB.x)

	detX := float64(eX)*float64(bB.y) - float64(eY)*float64(bB.x)
	detY := float64(bA.x)*float64(eY) - float64(bA.y)*float64(eX)

	x := detX / det
	y := detY / det

	// 245901639437.2623 == 245901639437 -> false ||  7806401274.0241995 == 7806401274 -> false
	if x != float64(int(x)) || y != float64(int(y)) {
		return 0
	}

	return int(x*3) + int(y)
}

func extractButton(l string) button {
	d := strings.Split(strings.Replace(l, ",", "", 1), " ")
	xV, _ := strconv.Atoi(strings.Replace(d[2], "X+", "", 1))
	yV, _ := strconv.Atoi(strings.Replace(d[3], "Y+", "", 1))
	return button{xV, yV}
}

func extractPrize(l string) (int, int) {
	d := strings.Split(strings.Replace(l, ",", "", 1), " ")
	xV, _ := strconv.Atoi(strings.Replace(d[1], "X=", "", 1))
	yV, _ := strconv.Atoi(strings.Replace(d[2], "Y=", "", 1))
	return xV, yV
}

type button struct {
	x int
	y int
}
