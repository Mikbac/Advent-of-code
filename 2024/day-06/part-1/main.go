package main

// Created by MikBac on 2024

import (
	"fmt"
	"slices"
	"utils/lineReader"
)

func main() {
	//lines := lineReader.ReadStringsFromFile("sample")
	lines := lineReader.ReadStringsFromFile("input")
	answer := solution(lines)

	fmt.Println("Answer:", answer)
}

func solution(lines []string) int {
	sp := position{}
	for pos1, line := range lines {
		for pos2, c := range line {
			if string(c) == "^" {
				sp = position{pos1, pos2}
			}
		}
	}

	visited := []position{sp}
	np, dir, inMap := makeStep(lines, sp, "^")
	visited = appendWithoutDuplicate(visited, np)
	for true {
		np, dir, inMap = makeStep(lines, np, dir)
		if inMap {
			visited = appendWithoutDuplicate(visited, np)
		} else {
			break
		}
	}

	return len(visited)
}

func makeStep(lines []string, pos position, dir string) (position, string, bool) {
	if dir == "^" && isInMap(position{pos.p1 - 1, pos.p2}, lines) {
		if string(lines[pos.p1-1][pos.p2]) != "#" {
			return position{pos.p1 - 1, pos.p2}, "^", true
		} else {
			return position{pos.p1, pos.p2}, ">", true
		}
	}

	if dir == ">" && isInMap(position{pos.p1, pos.p2 + 1}, lines) {
		if string(lines[pos.p1][pos.p2+1]) != "#" {
			return position{pos.p1, pos.p2 + 1}, ">", true
		} else {
			return position{pos.p1, pos.p2}, "v", true
		}
	}

	if dir == "v" && isInMap(position{pos.p1 + 1, pos.p2}, lines) {
		if string(lines[pos.p1+1][pos.p2]) != "#" {
			return position{pos.p1 + 1, pos.p2}, "v", true
		} else {
			return position{pos.p1, pos.p2}, "<", true
		}
	}

	if dir == "<" && isInMap(position{pos.p1, pos.p2 - 1}, lines) {
		if string(lines[pos.p1][pos.p2-1]) != "#" {
			return position{pos.p1, pos.p2 - 1}, "<", true
		} else {
			return position{pos.p1, pos.p2}, "^", true
		}
	}

	return position{}, "", false
}

func isInMap(pos position, lines []string) bool {
	return pos.p1 >= 0 && pos.p2 >= 0 && pos.p1 < len(lines) && pos.p2 < len(lines[0])
}

func appendWithoutDuplicate(positions []position, np position) []position {
	if !slices.Contains(positions, np) {
		return append(positions, np)
	} else {
		return positions
	}
}

type position struct {
	p1 int
	p2 int
}
