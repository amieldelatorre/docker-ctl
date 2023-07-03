# docker-ctl

Small Flask web server to control docker containers running on a machine using compose files

## To run
```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
waitress-serve --host 0.0.0.0 --call app:create_app
```
