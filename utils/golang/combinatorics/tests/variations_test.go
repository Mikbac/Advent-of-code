package tests

import (
	"testing"
	"utils/combinatorics"
)

func TestVariationsWithRepetition(t *testing.T) {
	values := combinatorics.VariationsWithRepetition([]string{"a", "b"}, 3, []string{})
	// [[a a a] [a a b] [a b a] [a b b] [b a a] [b a b] [b b a] [b b b]]

	if len(values) != 8 {
		t.Errorf("Expected 8 elements, but got \"%v\"", len(values))
	}
}
