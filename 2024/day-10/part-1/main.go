package main

// Created by MikBac on 2024

import (
	"fmt"
	"strconv"
	"utils/lineReader"
)

func main() {
	//lines := lineReader.ReadStringsFromFile("sample")
	lines := lineReader.ReadStringsFromFile("input")
	answer := solution(lines)

	fmt.Println("Answer:", answer)
}

func solution(lines []string) int {
	var th []position
	var ts []position
	var tm [][]int
	for i := 0; i < len(lines); i++ {
		tm = append(tm, []int{})
		for j := 0; j < len(lines); j++ {
			n, _ := strconv.Atoi(string(lines[i][j]))
			tm[i] = append(tm[i], n)
			if n == 0 {
				th = append(th, position{i, j})
			}
			if n == 9 {
				ts = append(ts, position{i, j})
			}
		}
	}

	sum := 0
	for _, p := range th {
		path := checkPath(p, tm, []position{})
		sum += calculateScore(path, ts)
	}

	return sum
}

func checkPath(cp position, tm [][]int, path []position) []position {

	if isAvailablePosition(cp, position{cp.x, cp.y + 1}, path, tm) {
		path = append(path, checkPath(position{cp.x, cp.y + 1}, tm, append(path, position{cp.x, cp.y + 1}))...)
	}
	if isAvailablePosition(cp, position{cp.x + 1, cp.y}, path, tm) {
		path = append(path, checkPath(position{cp.x + 1, cp.y}, tm, append(path, position{cp.x + 1, cp.y}))...)
	}
	if isAvailablePosition(cp, position{cp.x, cp.y - 1}, path, tm) {
		path = append(path, checkPath(position{cp.x, cp.y - 1}, tm, append(path, position{cp.x, cp.y - 1}))...)
	}
	if isAvailablePosition(cp, position{cp.x - 1, cp.y}, path, tm) {
		path = append(path, checkPath(position{cp.x - 1, cp.y}, tm, append(path, position{cp.x - 1, cp.y}))...)
	}

	return path
}

func isAvailablePosition(cp position, np position, path []position, tm [][]int) bool {
	if np.x >= 0 && np.y >= 0 && np.x < len(tm) && np.y < len(tm[0]) {
		if tm[cp.x][cp.y] == tm[np.x][np.y]-1 {
			for _, p := range path {
				if np == p {
					return false
				}
			}
			return true
		}
	}
	return false
}

func calculateScore(path []position, ts []position) int {
	sum := 0
	for _, p := range ts {
		for _, pp := range path {
			if p == pp {
				sum++
				break
			}
		}
	}
	return sum
}

type position struct {
	x int
	y int
}
