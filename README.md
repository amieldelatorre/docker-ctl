# docker-ctl

Small Flask web server to control docker containers running on a machine using compose files

## Service File
Populate the docker-ctl.service.example file with the correct values and rename it to docker-ctl.service. Create a copy of the file at `/etc/systemd/system/`
Then:
```bash
sudo systemctl daemon-reload
sudo systemctl enable docker-ctl.service
sudo systemctl start docker-ctl.service
sudo systemctl status docker-ctl.service
```

## To run
```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
waitress-serve --host 0.0.0.0 --port 5000 --call app:create_app
```

## Container for local development
```bash
docker build -t debian-local-dev --file Dockerfile.dev .
docker run -it --name debian-local-dev -v ${PWD}:/docker-ctl debian-local-dev /bin/bash
docker run -it --rm --name debian-local-dev -p 5000:8080 --privileged -v ${PWD}:/docker-ctl -e DOCKER_HOST='tcp://127.0.0.1:2375/' -e DOCKER_DRIVER='overlay' debian-local-dev /bin/sh
```