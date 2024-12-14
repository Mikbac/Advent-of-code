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

	//      84 * 10000000004245 - 21 * 10000000005634
	// x1 = ----------------------------------------- = 245901639437.2623
	//      40 * 84 - 38 * 21
	x1 := float64(bB.y*eX-bB.x*eY) / float64(bA.x*bB.y-bA.y*bB.x)

	//      40 * 10000000005634 - 38 * 10000000004245
	// x2 = ----------------------------------------- = 7806401274.0241995
	//      40 * 84 - 38 * 21
	x2 := float64(bA.x*eY-bA.y*eX) / float64(bA.x*bB.y-bA.y*bB.x)

	// 245901639437.2623 == 245901639437 -> false ||  7806401274.0241995 == 7806401274 -> false
	if x1 == float64(int(x1)) || x2 == float64(int(x2)) {
		return 0
	}

	return int(x1*3) + int(x2)
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
