package osinteractions

import (
	"errors"
	"fmt"
	"log"
	"os"
	"path/filepath"
)

var ComposeFileListPath = filepath.Join(getUserHomeDir(), ".config", "docker-ctl", "compose-files")

func CheckComposeFileListExists() (bool, error) {
	_, err := os.Stat(ComposeFileListPath)
	if err == nil {
		return true, nil
	} else if errors.Is(err, os.ErrNotExist) {
		return false, nil
	}

	return false, err
}

func getUserHomeDir() string {
	dir, err := os.UserHomeDir()
	if err != nil {
		fmt.Println("ERROR: Could not get user home directory")
		log.Fatal(err)
	}

	return dir
}
