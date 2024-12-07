package combinatorics

// VariationsWithRepetition input: []string{"+", "*", "||"}, 3, []string{}
// produces:
// [[+ + +] [+ + *] [+ * +] [+ * *] [* + +] [* + *] [* * +] [* * *]]
func VariationsWithRepetition(input []string, depth int, product []string) [][]string {
	if depth == len(product) {
		tmp := make([]string, len(product))
		copy(tmp, product)
		return [][]string{tmp}
	} else {
		var resp [][]string
		for _, i := range input {
			resp = append(resp, VariationsWithRepetition(input, depth, append(product, i))...)
		}
		return resp
	}
}
