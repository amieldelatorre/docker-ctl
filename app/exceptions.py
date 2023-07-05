from app.utils.compose_file_list import COMPOSE_FILE_LOCATION


class ComposeListFileNotFoundException(Exception):
    def __init__(self, msg=f"The compose file list in '{COMPOSE_FILE_LOCATION}' cannot be found."):
        super().__init__(msg)


class ComposeFileNotFoundException(Exception):
    def __init__(self, msg: str):
        super().__init__(msg)
