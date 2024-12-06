package tests

import (
	"testing"
	"utils/simpleFuncs"
)

func TestReadStringsFromFile(t *testing.T) {
	values := simpleFuncs.RemoveIndexFromSliceAndReturnString([]string{"a", "b", "c"}, 1)

	if values != "a c" {
		t.Errorf("Expected \"a c\", but got \"%v\"", values)
	}
}
