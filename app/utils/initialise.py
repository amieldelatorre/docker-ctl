from app.services.docker_interactions import get_containers_list
from app.utils.compose_file_list import compose_file_list_exists, COMPOSE_FILE_LOCATION
from python_on_whales import exceptions


def docker_is_available() -> bool:
    try:
        get_containers_list()
        return True
    except exceptions.DockerException as e:
        return False


def pre_run_checks() -> None:
    errors: list[str] = []

    if not docker_is_available():
        errors.append("ERROR: Please check that docker is installed or running")
    if not compose_file_list_exists():
        errors.append(f"ERROR: Could not find {COMPOSE_FILE_LOCATION}. Please create one")

    if errors:
        for error in errors:
            print(error)
        exit(1)
