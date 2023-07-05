import os
from app.models.compose_file import ComposeFile
from app.utils.compose_file_list import COMPOSE_FILE_LOCATION
from typing import Optional


class ComposeFileList:
    compose_files: list[ComposeFile]
    error: Optional[str]
    path: str = os.path.abspath(COMPOSE_FILE_LOCATION)

    def __init__(self, compose_files: list[ComposeFile], error: Optional[str]):
        self.compose_files = compose_files
        self.error = error
