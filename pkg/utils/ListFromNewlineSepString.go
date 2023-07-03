package utils

import "strings"

func GetListFromNewlineSepString(stringList string) []string {
	dataList := strings.Split(stringList, "\n")

	for i, item := range dataList {
		dataList[i] = strings.TrimSpace(item)
	}

	return dataList
}
