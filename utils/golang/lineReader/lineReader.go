package lineReader

import (
	"fmt"
	"os"
	"strings"
)

func ReadFromFile(filename string) []string {
	content, err := os.ReadFile(filename)
	if err != nil {
		//Do something
		fmt.Println(err)
		os.Exit(1)
	}
	lines := strings.Split(string(content), "\r\n")

	return lines
}
