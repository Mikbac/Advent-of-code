package simpleFuncs

func IntSubtractionAbs(v1 int, v2 int) int {
	if v1 > v2 {
		return v1 - v2
	} else {
		return v2 - v1
	}
}
