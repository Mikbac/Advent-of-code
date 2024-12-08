package tests

import (
	"testing"
	"utils/simpleFuncs"
)

func TestIntSubtractionAbs1(t *testing.T) {
	values := simpleFuncs.IntSubtractionAbs(3, 5)

	if values != 2 {
		t.Errorf("Expected 2, but got %v", values)
	}
}

func TestIntSubtractionAbs2(t *testing.T) {
	values := simpleFuncs.IntSubtractionAbs(-3, 5)

	if values != 8 {
		t.Errorf("Expected 8, but got %v", values)
	}
}

func TestIntSubtractionAbs3(t *testing.T) {
	values := simpleFuncs.IntSubtractionAbs(5, -3)

	if values != 8 {
		t.Errorf("Expected 8, but got %v", values)
	}
}

func TestIntSubtractionAbs4(t *testing.T) {
	values := simpleFuncs.IntSubtractionAbs(3, 3)

	if values != 0 {
		t.Errorf("Expected 0, but got %v", values)
	}
}
