import os

COMPOSE_FILE_LOCATION = os.path.join(os.path.expanduser("~"), ".config", "docker-ctl", "compose-files")


def check_compose_file_list_exists() -> None:
    if not check_file_exists(COMPOSE_FILE_LOCATION):
        print(f"ERROR: Could not find {COMPOSE_FILE_LOCATION}. Please create one")
        exit(1)

def check_file_exists(filepath: str) -> bool:
    return os.path.exists(filepath)
