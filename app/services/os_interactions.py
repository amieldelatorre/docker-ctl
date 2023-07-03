from app.utils.compose_file_list import COMPOSE_FILE_LOCATION, check_compose_file_list_exists, check_file_exists

def get_compose_file_paths() -> list[str]:
    if not check_compose_file_list_exists:
        return None
    
    file = open(COMPOSE_FILE_LOCATION, "r")
    file_contents = file.readlines()
    file.close()

    path = []
    for item in file_contents:
        path.append(item.strip())

    return path
