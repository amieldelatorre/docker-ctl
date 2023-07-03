package main

import (
	"flag"
	"log"
	"net/http"
	"os"
	"time"
)

func main() {
	port := flag.String("port", "4000", "Port for the web server")
	flag.Parse()

	infoLog := log.New(os.Stdout, "INFO\t", log.Ldate|log.Ltime)
	errorLog := log.New(os.Stderr, "ERROR\t", log.Ldate|log.Ltime|log.Lshortfile)

	app := application{
		errorLog: errorLog,
		infoLog:  infoLog,
		addr:     ":" + *port,
	}

	server := &http.Server{
		Addr:         app.addr,
		ErrorLog:     app.errorLog,
		IdleTimeout:  time.Minute,
		ReadTimeout:  5 * time.Second,
		WriteTimeout: 10 * time.Second,
		Handler:      app.routes(),
	}

	infoLog.Printf("Starting server on %s", app.addr)
	err := server.ListenAndServe()
	errorLog.Fatal(err)

	// log.SetFlags(log.LstdFlags | log.Lshortfile)
	// infoLog.Println(fmt.Sprintf("Checking if %s exists", osinteractions.ComposeFileListPath))

	//fmt.Println(composeFileAndServices)

	// fmt.Println(dockerinteractions.CheckContainerExists("nginx"))

	// out, err := exec.Command("docker", "compose", "--file", "/home/amiel/Git/amiel-tools/compose.yml", "config", "--services").Output()
	// if err != nil {
	// 	log.Fatal(err)
	// }

	// compose_containers := strings.Split(strings.TrimSpace(string(out)), "\n")
	// fmt.Println(compose_containers)

	// out, err = exec.Command("docker", "inspect", "nginx").Output()
	// if err != nil {
	// 	log.Fatal(err)
	// }

	// fmt.Println(string(out))

	// fmt.Println(filepath.Dir("/home/amiel/Git/amiel-tools/compose.yml"))
	// os.Chdir("/home/amiel/Git")
	// cwd, err := os.Getwd()
	// if err != nil {
	// 	log.Fatal(err)
	// }
	// fmt.Println(cwd)
}
