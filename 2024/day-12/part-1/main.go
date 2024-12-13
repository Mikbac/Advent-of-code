package main

// Created by MikBac on 2024

import (
	"fmt"
	"utils/lineReader"
)

var visitedList []position

func main() {
	//lines := lineReader.ReadStringsFromFile("sample1")
	//lines := lineReader.ReadStringsFromFile("sample2")
	//lines := lineReader.ReadStringsFromFile("sample3")
	lines := lineReader.ReadStringsFromFile("input")
	answer := solution(lines)

	fmt.Println("Answer:", answer)
}

func solution(lines []string) int {
	fields := make(map[position]field)
	for i := 0; i < len(lines); i++ {
		for j := 0; j < len(lines[i]); j++ {
			fields[position{i, j}] = field{getNeighborhood(i, j, lines), getPerimeter(i, j, lines)}
		}
	}

	var fieldsSets [][]position
	for i := 0; i < len(lines); i++ {
		for j := 0; j < len(lines[i]); j++ {
			visited := false
			p := position{i, j}
			for _, fs := range fieldsSets {
				for _, f := range fs {
					if p == f {
						visited = true
					}

				}
			}
			if visited {
				continue
			}
			visitedList = []position{}
			fieldsSets = append(fieldsSets, getPath(p, fields))
		}
	}

	ans := 0
	for _, fs := range fieldsSets {
		ans += calcFields(fs, fields)
	}

	return ans
}

func calcFields(fs []position, fields map[position]field) int {
	var visited []position
	aq := 0
	pq := 0

	for _, f := range fs {
		iv := false
		for _, v := range visited {
			if f == v {
				iv = true
				break
			}
		}
		if iv {
			continue
		}
		aq++
		pq += fields[f].peri
		visited = append(visited, f)

	}

	return aq * pq
}

func getPath(p position, fields map[position]field) []position {
	for _, v := range visitedList {
		if p == v {
			return []position{}
		}
	}
	visitedList = append(visitedList, p)
	n := []position{p}
	for _, pp := range fields[p].nei {
		n = append(n, getPath(pp, fields)...)
	}

	return n
}

func getNeighborhood(i int, j int, lines []string) []position {
	var n []position
	if isAvailable(i, j+1, lines) && lines[i][j] == lines[i][j+1] {
		n = append(n, position{i, j + 1})
	}
	if isAvailable(i, j-1, lines) && lines[i][j] == lines[i][j-1] {
		n = append(n, position{i, j - 1})
	}
	if isAvailable(i+1, j, lines) && lines[i][j] == lines[i+1][j] {
		n = append(n, position{i + 1, j})
	}
	if isAvailable(i-1, j, lines) && lines[i][j] == lines[i-1][j] {
		n = append(n, position{i - 1, j})
	}
	return n
}

func getPerimeter(i int, j int, lines []string) int {
	p := 0
	if !isAvailable(i, j+1, lines) || lines[i][j] != lines[i][j+1] {
		p++
	}
	if !isAvailable(i, j-1, lines) || lines[i][j] != lines[i][j-1] {
		p++
	}
	if !isAvailable(i+1, j, lines) || lines[i][j] != lines[i+1][j] {
		p++
	}
	if !isAvailable(i-1, j, lines) || lines[i][j] != lines[i-1][j] {
		p++
	}
	return p
}

func isAvailable(i int, j int, lines []string) bool {
	if i >= 0 && j >= 0 && i < len(lines) && j < len(lines[0]) {
		return true
	}
	return false
}

type field struct {
	nei  []position
	peri int
}

type position struct {
	x int
	y int
}
