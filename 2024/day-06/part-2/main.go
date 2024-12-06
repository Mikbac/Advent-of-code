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
				sp = position{pos1, pos2, "^"}
			}
		}
	}

	vp := searchBasicPath(lines, sp, position{-1, -1, ""})

	cc := 0
	for _, p := range vp {
		if !(sp.p1 == p.p1 && sp.p2 == p.p2) {
			ic := searchCycles(lines, sp, position{p.p1, p.p2, ""})
			if ic {
				cc++
			}
		}
	}

	return cc
}

func searchBasicPath(lines []string, sp position, obs position) []position {
	var visited []position
	np, inMap := makeStep(lines, sp, obs)
	visited, _ = appendWithoutDuplicate(visited, position{np.p1, np.p2, ""})
	for true {
		np, inMap = makeStep(lines, np, obs)
		if inMap {
			visited, _ = appendWithoutDuplicate(visited, position{np.p1, np.p2, ""})
		} else {
			break
		}
	}

	return visited
}

func searchCycles(lines []string, sp position, obs position) bool {
	np, inMap := makeStep(lines, sp, obs)
	visited, isCycle := appendWithoutDuplicate([]position{}, np)
	for true {
		np, inMap = makeStep(lines, np, obs)
		if inMap {
			visited, isCycle = appendWithoutDuplicate(visited, np)
			if isCycle {
				return true
			}
		} else {
			break
		}
	}
	return false
}

func makeStep(lines []string, pos position, obs position) (position, bool) {
	if pos.dir == "^" && isInMap(position{pos.p1 - 1, pos.p2, pos.dir}, lines) {
		if string(lines[pos.p1-1][pos.p2]) != "#" && isNewObs(position{pos.p1 - 1, pos.p2, ""}, obs) {
			return position{pos.p1 - 1, pos.p2, "^"}, true
		} else {
			return position{pos.p1, pos.p2, ">"}, true
		}
	}

	if pos.dir == ">" && isInMap(position{pos.p1, pos.p2 + 1, pos.dir}, lines) {
		if string(lines[pos.p1][pos.p2+1]) != "#" && isNewObs(position{pos.p1, pos.p2 + 1, ""}, obs) {
			return position{pos.p1, pos.p2 + 1, ">"}, true
		} else {
			return position{pos.p1, pos.p2, "v"}, true
		}
	}

	if pos.dir == "v" && isInMap(position{pos.p1 + 1, pos.p2, pos.dir}, lines) {
		if string(lines[pos.p1+1][pos.p2]) != "#" && isNewObs(position{pos.p1 + 1, pos.p2, ""}, obs) {
			return position{pos.p1 + 1, pos.p2, "v"}, true
		} else {
			return position{pos.p1, pos.p2, "<"}, true
		}
	}

	if pos.dir == "<" && isInMap(position{pos.p1, pos.p2 - 1, pos.dir}, lines) {
		if string(lines[pos.p1][pos.p2-1]) != "#" && isNewObs(position{pos.p1, pos.p2 - 1, ""}, obs) {
			return position{pos.p1, pos.p2 - 1, "<"}, true
		} else {
			return position{pos.p1, pos.p2, "^"}, true
		}
	}

	return position{}, false
}

func isInMap(pos position, lines []string) bool {
	return pos.p1 >= 0 && pos.p2 >= 0 && pos.p1 < len(lines) && pos.p2 < len(lines[0])
}

func appendWithoutDuplicate(positions []position, np position) ([]position, bool) {
	if !slices.Contains(positions, np) {
		return append(positions, np), false
	} else {
		return positions, true
	}
}

func isNewObs(pos position, obs position) bool {
	return !(pos.p1 == obs.p1 && pos.p2 == obs.p2)
}

type position struct {
	p1  int
	p2  int
	dir string
}
