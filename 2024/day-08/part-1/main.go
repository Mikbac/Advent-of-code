package main

// Created by MikBac on 2024

import (
	"fmt"
	"slices"
	"utils/lineReader"
	"utils/simpleFuncs"
)

func main() {
	//lines := lineReader.ReadStringsFromFile("sample1")
	//lines := lineReader.ReadStringsFromFile("sample2")
	lines := lineReader.ReadStringsFromFile("input")
	answer := solution(lines)

	fmt.Println("Answer:", answer)
}

func solution(lines []string) int {
	am := map[string][]point{}

	for xp, line := range lines {
		for yp, c := range line {
			if string(c) != "." {
				am[string(c)] = append(am[string(c)], point{xp, yp})
			}
		}
	}

	var antiPoints []point
	for k := range am {
		for _, p := range generateAllAntinode(am[k]) {

			d1 := simpleFuncs.IntSubtractionAbs(p[0].x, p[1].x)
			d2 := simpleFuncs.IntSubtractionAbs(p[0].y, p[1].y)

			// 1
			if p[0].x > p[1].x && p[0].y < p[1].y {
				antiPoints = append(antiPoints, point{p[0].x + d1, p[0].y - d2})
			}
			if p[1].x > p[0].x && p[1].y < p[0].y {
				antiPoints = append(antiPoints, point{p[1].x + d1, p[1].y - d2})
			}
			// 2
			if p[0].x < p[1].x && p[0].y > p[1].y {
				antiPoints = append(antiPoints, point{p[0].x - d1, p[0].y + d2})
			}
			if p[1].x < p[0].x && p[1].y > p[0].y {
				antiPoints = append(antiPoints, point{p[1].x - d1, p[1].y + d2})
			}
			// 3
			if p[0].x > p[1].x && p[0].y > p[1].y {
				antiPoints = append(antiPoints, point{p[0].x + d1, p[0].y + d2})
			}
			if p[1].x > p[0].x && p[1].y > p[0].y {
				antiPoints = append(antiPoints, point{p[1].x + d1, p[1].y + d2})
			}
			// 4
			if p[0].x < p[1].x && p[0].y < p[1].y {
				antiPoints = append(antiPoints, point{p[0].x - d1, p[0].y - d2})
			}
			if p[1].x < p[0].x && p[1].y < p[0].y {
				antiPoints = append(antiPoints, point{p[1].x - d1, p[1].y - d2})
			}
		}
	}

	var antiPointsAns []point
	for _, p := range antiPoints {
		if p.x >= 0 && p.y >= 0 && p.x < len(lines) && p.y < len(lines[0]) && !(slices.Contains(antiPointsAns, p)) {
			antiPointsAns = append(antiPointsAns, p)
		}
	}

	return len(antiPointsAns)
}

func generateAllAntinode(ps []point) [][]point {
	var ans [][]point
	for i, p1 := range ps {
		for _, p2 := range ps[:i] {
			if p1 != p2 {
				ans = append(ans, []point{p1, p2})
			}
		}
	}
	return ans
}

type point struct {
	x int
	y int
}
