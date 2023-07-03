package main

import (
	"log"
	"net/http"
	"text/template"

	"github.com/amieldelatorre/docker-ctl/pkg/handlers"
	"github.com/amieldelatorre/docker-ctl/ui"
	"github.com/go-chi/chi/v5"
)

type application struct {
	errorLog      *log.Logger
	infoLog       *log.Logger
	addr          string
	templateCache map[string]*template.Template
}

func (app *application) routes() http.Handler {
	router := chi.NewRouter()

	fileServer := http.FileServer(http.FS(ui.Files))

	router.Handle("/static/*filepath", fileServer)
	router.Get("/ping", handlers.GetPing)
	router.Get("/", handlers.GetHome)

	return router
}
