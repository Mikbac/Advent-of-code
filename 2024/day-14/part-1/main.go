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

	for i := 0; i < 100; i++ {
		for i, r := range robots {
			robots[i] = updateRobotPosition(r)
		}
	}

	return calculateQuadrants(robots)

}

func calculateQuadrants(robots []robot) int {
	q1 := 0
	q2 := 0
	q3 := 0
	q4 := 0

	for _, r := range robots {
		if r.p.x < wide/2 && r.p.y < tall/2 {
			q1++
		}
		if r.p.x > wide/2 && r.p.y < tall/2 {
			q2++
		}
		if r.p.x < wide/2 && r.p.y > tall/2 {
			q3++
		}
		if r.p.x > wide/2 && r.p.y > tall/2 {
			q4++
		}

	}

	return q1 * q2 * q3 * q4
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
