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

		ans += findOptimal(bA, bB, eX, eY)
	}

	return ans
}

func findOptimal(bA button, bB button, eX int, eY int) int {
	coins := 0
	aCounter := 0
	for aCounter*bA.x <= eX && aCounter*bA.y <= eY {
		bCounter := 0
		for bCounter*bB.x <= eX && bCounter*bB.y <= eY {
			if aCounter*bA.x+bCounter*bB.x == eX && aCounter*bA.y+bCounter*bB.y == eY {
				cc := aCounter*3 + bCounter
				if cc < coins || coins == 0 {
					coins = cc
				}
			}
			bCounter++
		}
		aCounter++
	}
	return coins
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
