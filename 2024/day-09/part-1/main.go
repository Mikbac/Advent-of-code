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
	answer := solution(lines[0])

	fmt.Println("Answer:", answer)
}

func solution(line string) int {
	var files []file
	isFile := true
	idCounter := 0
	for _, c := range line {
		s, _ := strconv.Atoi(string(c))
		if isFile {
			files = append(files, file{idCounter, s})
			idCounter++
			isFile = false
		} else {
			files = append(files, file{-1, s})
			isFile = true
		}
	}

	for isAnyToDo(files) {
		isB := false
		for i := len(files) - 1; i >= 0; i-- {
			if files[i].id != -1 && files[i].value != 0 {
				for j := 0; j < len(files); j++ {
					if files[j].id == -1 && files[j].value != 0 {
						if files[i].value >= files[j].value {
							files[j] = file{files[i].id, files[j].value}
							files[i].value = files[i].value - files[j].value
							isB = true
						} else {
							diff := files[i].value
							files[j].value -= files[i].value
							files[i].value = 0
							files = append(files[:j], append([]file{{files[i].id, diff}}, files[j:]...)...)
							isB = true
						}
					}
					if isB {
						break
					}
				}
			}
			if isB {
				break
			}
		}
	}

	ans := 0
	c := 0
	for _, f := range files {
		if f.id != -1 && f.value != 0 {
			for i := 0; i < f.value; i++ {
				ans += c * f.id
				c++
			}
		}
	}

	return ans
}

func isAnyToDo(files []file) bool {
	for i := 0; i < len(files)-1; i++ {
		if files[i].id == -1 && files[i].value != 0 && files[i+1].id != -1 && files[i+1].value != 0 {
			return true
		}
	}
	return false
}

type file struct {
	id    int
	value int
}