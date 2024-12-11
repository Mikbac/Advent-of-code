package main

// Created by MikBac on 2024

import (
	"fmt"
	"strconv"
	"strings"
	"utils/lineReader"
)

var exLvl = 75
var ansL []ansEnt

func main() {
	//lines := lineReader.ReadStringsFromFile("sample1")
	//lines := lineReader.ReadStringsFromFile("sample2")
	lines := lineReader.ReadStringsFromFile("input")
	answer := solution(lines[0])

	fmt.Println("Answer:", answer)
}

func solution(line string) int {
	var stones []int
	for _, c := range strings.Split(line, " ") {
		n, _ := strconv.Atoi(c)
		stones = append(stones, n)
	}

	sum := 0
	for _, s := range stones {
		sum += updateStones(s, 0)
	}

	return sum
}

func updateStones(stone int, lvl int) int {
	for _, e := range ansL {
		if e.lvl == lvl && e.stone == stone {
			return e.val
		}
	}

	if lvl == exLvl {
		return 1
	}

	sum := 0
	if stone == 0 {
		sum += updateStones(1, lvl+1)
	} else if len(strconv.Itoa(stone))%2 == 0 {
		s := strconv.Itoa(stone)
		n1, _ := strconv.Atoi(s[:len(s)/2])
		n2, _ := strconv.Atoi(s[len(s)/2:])
		sum += updateStones(n1, lvl+1)
		sum += updateStones(n2, lvl+1)
	} else {
		sum += updateStones(stone*2024, lvl+1)
	}

	ansL = append(ansL, ansEnt{lvl, stone, sum})
	return sum
}

type ansEnt struct {
	lvl   int
	stone int
	val   int
}
