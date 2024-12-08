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
	ab := []point{}

	for xp, line := range lines {
		for yp, c := range line {
			if string(c) != "." {
				am[string(c)] = append(am[string(c)], point{xp, yp})
				ab = append(ab, point{xp, yp})
			}
		}
	}

	antiPoints := ab
	for k := range am {
		for _, p := range generateAllAntinode(am[k]) {

			d1 := simpleFuncs.IntSubtractionAbs(p[0].x, p[1].x)
			d2 := simpleFuncs.IntSubtractionAbs(p[0].y, p[1].y)

			// 1
			if p[0].x > p[1].x && p[0].y < p[1].y {
				antiPoints = append(antiPoints, createPointWithTrend(lines, p[0], d1, -d2)...)
			}
			if p[1].x > p[0].x && p[1].y < p[0].y {
				antiPoints = append(antiPoints, createPointWithTrend(lines, p[1], d1, -d2)...)
			}
			// 2
			if p[0].x < p[1].x && p[0].y > p[1].y {
				antiPoints = append(antiPoints, createPointWithTrend(lines, p[0], -d1, d2)...)
			}
			if p[1].x < p[0].x && p[1].y > p[0].y {
				antiPoints = append(antiPoints, createPointWithTrend(lines, p[1], -d1, d2)...)
			}
			// 3
			if p[0].x > p[1].x && p[0].y > p[1].y {
				antiPoints = append(antiPoints, createPointWithTrend(lines, p[0], d1, d2)...)
			}
			if p[1].x > p[0].x && p[1].y > p[0].y {
				antiPoints = append(antiPoints, createPointWithTrend(lines, p[1], d1, d2)...)
			}
			// 4
			if p[0].x < p[1].x && p[0].y < p[1].y {
				antiPoints = append(antiPoints, createPointWithTrend(lines, p[0], -d1, -d2)...)
			}
			if p[1].x < p[0].x && p[1].y < p[0].y {
				antiPoints = append(antiPoints, createPointWithTrend(lines, p[1], -d1, -d2)...)
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

func createPointWithTrend(lines []string, p point, xt int, yt int) []point {
	tp := p
	var points []point
	for tp.x >= 0 && tp.y >= 0 && tp.x < len(lines) && tp.y < len(lines[0]) {
		tp.x += xt
		tp.y += yt
		points = append(points, point{tp.x, tp.y})
	}
	return points
}

type point struct {
	x int
	y int
}
