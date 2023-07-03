package dockerinteractions

import (
	"bytes"
	"fmt"
	"os/exec"
	"strings"
)

func CheckContainerExists(ctName string) (bool, error) {
	ctFilterBytes, err := exec.Command("docker", "container", "ls", "-a", "--format", "'{{.Names}}'", "--filter", fmt.Sprintf("name=^%s$", ctName)).Output()
	if err != nil {
		return false, err
	}

	ctFilterResults := (string(bytes.TrimSpace(ctFilterBytes)))

	if strings.Trim(ctFilterResults, "'") != ctName {
		return false, nil
	}

	return true, nil
}
