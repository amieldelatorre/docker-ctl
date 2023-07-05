from app.utils.compose_file_list import COMPOSE_FILE_LOCATION, compose_file_list_exists, file_exists

def get_compose_file_paths() -> list[str]:
    if not compose_file_list_exists:
        print(f"ERROR: Could not find {COMPOSE_FILE_LOCATION}. Please create one")
        exit(1)
    
    file = open(COMPOSE_FILE_LOCATION, "r")
    file_contents = file.readlines()
    file.close()

    path = []
    for item in file_contents:
        path.append(item.strip())

    return path
