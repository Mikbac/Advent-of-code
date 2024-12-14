package main

// Created by MikBac on 2024

import (
	"fmt"
	"strconv"
	"strings"
	"utils/lineReader"
)

//var tall = 7
//var wide = 11

var tall = 103
var wide = 101

func main() {
	//lines := lineReader.ReadStringsFromFile("sample")
	lines := lineReader.ReadStringsFromFile("input")
	answer := solution(lines)

	fmt.Println("Answer:", answer)
}

func solution(lines []string) int {
	var robots []robot
	for _, line := range lines {
		robots = append(robots, convertLine(line))
	}

	inc := 1
	for true {
		for i, r := range robots {
			robots[i] = updateRobotPosition(r)
		}
		isTree := findTree(robots)

		if isTree {
			break
		} else {
			inc++
		}
	}

	return inc
}

func findTree(robots []robot) bool {
	places := []position{}

	for _, r := range robots {
		for _, p := range places {
			if p == r.p {
				return false
			}
		}
		places = append(places, r.p)
	}

	tm := [][]string{}

	for t := 0; t < tall; t++ {
		l := []string{}
		for w := 0; w < wide; w++ {
			l = append(l, ".")
		}
		tm = append(tm, l)
	}

	for _, r := range robots {
		tm[r.p.y][r.p.x] = "*"
	}

	for _, tmm := range tm {
		fmt.Println(strings.Join(tmm, ""))
	}

	return true
}

func updateRobotPosition(r robot) robot {

	px := r.p.x + r.x
	py := r.p.y + r.y

	if px >= wide {
		px = px - wide
	}
	if px < 0 {
		px = wide + px
	}
	if py >= tall {
		py = py - tall
	}
	if py < 0 {
		py = tall + py
	}

	return robot{position{px, py}, r.x, r.y}
}

func convertLine(l string) robot {
	sl := strings.Split(l, " ")
	pc := strings.Split(strings.Replace(sl[0], "p=", "", 1), ",")
	px, _ := strconv.Atoi(pc[0])
	py, _ := strconv.Atoi(pc[1])

	vc := strings.Split(strings.Replace(sl[1], "v=", "", 1), ",")
	vx, _ := strconv.Atoi(vc[0])
	vy, _ := strconv.Atoi(vc[1])

	return robot{position{px, py}, vx, vy}
}

type robot struct {
	p position
	x int
	y int
}

type position struct {
	x int
	y int
}
