package dockerinteractions

import (
	"bytes"
	"os/exec"

	"github.com/amieldelatorre/docker-ctl/pkg/models"
	"github.com/amieldelatorre/docker-ctl/pkg/utils"
)

func GetComposeFileContainers(filepath string) (map[string]models.Service, error) {
	composeInfo := make(map[string]models.Service)

	containersBytes, err := exec.Command("docker", "compose", "--file", filepath, "config", "--services").Output()
	if err != nil {
		return composeInfo, err
	}

	containersList := utils.GetListFromNewlineSepString(string(bytes.TrimSpace(containersBytes)))

	for _, container := range containersList {
		composeInfo[container], err = GetContainerInfo(container)
		if err != nil {
			return composeInfo, err
		}
	}
	return composeInfo, nil
}
