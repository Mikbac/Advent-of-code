package simpleFuncs

import "strings"

func RemoveIndexFromSliceAndReturnString(s []string, index int) string {
	tmp := make([]string, len(s))
	copy(tmp, s)
	return strings.Join(append(tmp[:index], tmp[index+1:]...), " ")
}
