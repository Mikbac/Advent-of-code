package tests

import (
	"testing"
	"utils/lineReader"
)

func TestReadStringsFromFile(t *testing.T) {
	lines := lineReader.ReadStringsFromFile("TestFile-string")
	if len(lines) != 6 {
		t.Errorf("Expected 6 lines, but got %v", len(lines))
	}

	if lines[0] != "111" {
		t.Errorf("Expected first value \"111\", but got %v", lines[len(lines)-1])
	}

	if lines[len(lines)-1] != "ccc" {
		t.Errorf("Expected last value \"ccc\", but got %v", lines[len(lines)-1])
	}
}

func TestReadIntsFromFile(t *testing.T) {
	numbers := lineReader.ReadIntsFromFile("TestFile-int")
	if len(numbers) != 7 {
		t.Errorf("Expected 7 numbers, but got %v", len(numbers))
	}
	if numbers[0] != 1 {
		t.Errorf("Expected first value 1, but got %v", numbers[len(numbers)-1])
	}

	if numbers[len(numbers)-1] != 99 {
		t.Errorf("Expected last value 999, but got %v", numbers[len(numbers)-1])
	}
}
