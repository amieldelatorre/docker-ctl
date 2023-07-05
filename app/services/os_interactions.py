from app.utils.compose_file_list import COMPOSE_FILE_LOCATION, compose_file_list_exists, file_exists
from typing import Optional


def get_compose_file_paths() -> Optional[list[str]]:
    if not compose_file_list_exists:
        return None
    
    file = open(COMPOSE_FILE_LOCATION, "r")
    file_contents = file.readlines()
    file.close()

    path = []
    for item in file_contents:
        path.append(item.strip())

    return path
