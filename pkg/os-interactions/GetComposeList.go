package osinteractions

import (
	"bytes"
	"os"

	"github.com/amieldelatorre/docker-ctl/pkg/utils"
)

func GetComposeList() ([]string, error) {
	rawData, err := os.ReadFile(ComposeFileListPath)
	if err != nil {
		return []string{}, err
	}

	dataString := string(bytes.TrimSpace(rawData))
	dataList := utils.GetListFromNewlineSepString(dataString)

	return dataList, nil
}
