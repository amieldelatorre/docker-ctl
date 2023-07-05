import os

COMPOSE_FILE_LOCATION = os.path.join(os.path.expanduser("~"), ".config", "docker-ctl", "compose-files")


def compose_file_list_exists() -> bool:
    return file_exists(COMPOSE_FILE_LOCATION)


def file_exists(filepath: str) -> bool:
    return os.path.exists(filepath)
