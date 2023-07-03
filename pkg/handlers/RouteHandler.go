package handlers

import (
	"fmt"
	"log"
	"net/http"
	"os"

	dockerinteractions "github.com/amieldelatorre/docker-ctl/pkg/docker-interactions"
	"github.com/amieldelatorre/docker-ctl/pkg/models"
	osinteractions "github.com/amieldelatorre/docker-ctl/pkg/os-interactions"
)

func GetHome(w http.ResponseWriter, r *http.Request) {
	composeFileListExists, err := osinteractions.CheckComposeFileListExists()
	if err != nil {
		log.Fatal(err)
	} else if !composeFileListExists {
		fileMissingMessage := fmt.Sprintf("%s does not exist. Please create one first", osinteractions.ComposeFileListPath)
		fmt.Println(fileMissingMessage)
		os.Exit(1)
	}

	composeList, err := osinteractions.GetComposeList()
	if err != nil {
		log.Fatal(err)
	}

	composeFilesAndServices := make(map[string]map[string]models.Service)

	for _, composeFile := range composeList {
		fmt.Println(composeFile)
		composeFilesAndServices[composeFile], err = dockerinteractions.GetComposeFileContainers(composeFile)
		if err != nil {
			log.Fatal(err)
		}
	}

}

func GetPing(w http.ResponseWriter, r *http.Request) {
	w.Write([]byte("Pong"))
}
