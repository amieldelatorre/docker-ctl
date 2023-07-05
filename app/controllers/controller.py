from flask import Blueprint,render_template, redirect
from app.models.service import Service
from app.services.docker_interactions import get_compose_files_info, compose_files_down, compose_files_up

ctl_blueprint = Blueprint('ctl_bp', __name__)


@ctl_blueprint.route("/")
def home():
    compose_files_info: dict[str, list[Service]] = get_compose_files_info()
    print(compose_files_info)
    
    return render_template(
        'home.html',
        title="home",
        compose_files_info=compose_files_info
    )


@ctl_blueprint.route("/down")
def down():
    compose_files_down()
    return redirect("/")


@ctl_blueprint.route("/up")
def up():
    compose_files_up()
    return redirect("/")


@ctl_blueprint.route("/ping")
def ping():
    return "pong"
