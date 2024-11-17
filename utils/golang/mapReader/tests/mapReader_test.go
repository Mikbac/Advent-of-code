package tests

import (
	"testing"
	"utils/mapReader"
)

func TestReadStringsFromFile(t *testing.T) {
	values := mapReader.ReadFromFile("TestFile-string-string", " ")
	if len(values) != 4 {
		t.Errorf("Expected 4 values, but got %v", len(values))
	}

	if values["aaa"] != "a1" {
		t.Errorf("Expected value \"a1\", but got %v", values["aaa"])
	}

	if values["ddd"] != "d5" {
		t.Errorf("Expected value \"d5\", but got %v", values["aaa"])
	}
}
