package mapReader

import (
	"fmt"
	"os"
	"strings"
)

func ReadFromFile(filename string, separator string) map[string]string {
	content, err := os.ReadFile(filename)
	if err != nil {
		//Do something
		fmt.Println(err)
		os.Exit(1)
	}
	lines := strings.Split(string(content), "\r\n")

	values := map[string]string{}
	for _, line := range lines {
		lv := strings.Split(line, separator)
		if len(lv) == 2 {
			values[lv[0]] = lv[1]
		}
	}

	return values
}
