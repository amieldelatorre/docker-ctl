from app.models.service import Service


class ComposeFile:
    parent_dir: str
    path: str
    error: str
    services: list[Service]

    def __init__(self, parent_dir: str, path: str, error: str, services: list[Service]):
        self.parent_dir: str = parent_dir
        self.path = path
        self.error = error
        self. services = services
