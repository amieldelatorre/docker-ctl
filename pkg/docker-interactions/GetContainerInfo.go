package dockerinteractions

import (
	"bytes"
	"encoding/json"
	"os/exec"

	"github.com/amieldelatorre/docker-ctl/pkg/models"
)

func GetContainerInfo(ctName string) (models.Service, error) {
	ctExists, err := CheckContainerExists(ctName)
	if err != nil {
		return models.Service{}, err
	}

	if !ctExists {
		return models.Service{Name: ctName, Status: "NotFound"}, nil
	}

	ctInfoBytes, err := exec.Command("docker", "inspect", ctName).Output()
	if err != nil {
		return models.Service{}, err
	}

	var ctInfoJson []map[string]any
	json.Unmarshal(bytes.TrimSpace(ctInfoBytes), &ctInfoJson)

	status := (ctInfoJson[0]["State"].(map[string]any)["Status"]).(string)

	return models.Service{Name: ctName, Status: status}, nil
}
