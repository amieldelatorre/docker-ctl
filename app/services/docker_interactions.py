from app.models.compose_file import ComposeFile
from app.models.compose_file_list import ComposeFileList
from app.models.service import Service
from app.services.os_interactions import get_compose_file_paths
from app.utils.compose_file_list import file_exists
from python_on_whales import DockerClient, docker, Container, exceptions
from pathlib import Path
from os.path import basename
from typing import Optional
from app.exceptions import ComposeListFileNotFoundException, ComposeFileNotFoundException


def get_compose_files_info() -> ComposeFileList:
    compose_file_paths: Optional[list[str]] = get_compose_file_paths()
    if compose_file_paths is None:
        return ComposeFileList(compose_files=[], error=str(ComposeListFileNotFoundException()))

    compose_file_list: list[ComposeFile] = []

    for compose_file_path in compose_file_paths:
        compose_file_dir = basename(Path(compose_file_path).parent)
        service_names_and_container_names: Optional[dict[str, str]] = get_services_for_compose(compose_file_path)

        if service_names_and_container_names is None:
            cf = ComposeFile(
                parent_dir=compose_file_dir,
                path=compose_file_path,
                error=str(ComposeFileNotFoundException(f"The compose file in '{compose_file_path}' cannot be found or "
                                                       f"is not valid")),
                services=[]
            )

            compose_file_list.append(cf)
            continue

        services_info: list[Service] = get_services_info(service_names_and_container_names)
        cf = ComposeFile(
            parent_dir=compose_file_dir,
            path=compose_file_path,
            error="",
            services=services_info
        )
        compose_file_list.append(cf)

    return ComposeFileList(
        compose_files=compose_file_list,
        error=None
    )


def get_services_info(srvc_names_and_ct_names: dict[str, str]) -> list[Service]:
    services_info: list[Service] = []
    for service_name in srvc_names_and_ct_names.keys():
        info: Service = get_srvc_info(service_name=service_name, container_name=srvc_names_and_ct_names[service_name])
        services_info.append(info)

    return services_info


def get_services_for_compose(compose_file_path: str) -> Optional[dict[str, str]]:
    if not file_exists(compose_file_path):
        return None

    docker_client = DockerClient(compose_files=[compose_file_path])
    try:
        compose_config = docker_client.compose.config(return_json=True)
    except exceptions.DockerException as e:
        return None

    services_config = compose_config["services"]

    services: dict[str, str] = {}
    for name in services_config.keys():
        services[name] = services_config[name]["container_name"]
    
    return services


def get_srvc_info(service_name: str, container_name: str) -> Service:
    if not container_exists(container_name):
        return Service(
            service_name=service_name, 
            container_name=container_name, 
            container_status="notFound"
            )
    
    container_status = get_container_status(container_name)

    return Service(
            service_name=service_name, 
            container_name=container_name, 
            container_status=container_status
            )


def container_exists(container_name: str) -> bool:
    containers = docker.container.list(all=True, filters={"name": container_name})
    for container in containers:
        if container_name == container.name:
            return True
        
    return False


def get_container_status(container_name: str) -> str:
    info = docker.container.inspect(container_name)
    return info.state.status


def compose_files_down():
    compose_file_paths: list[str] = get_compose_file_paths()

    for file in compose_file_paths:
        if not file_exists(file):
            continue
        docker_client = DockerClient(compose_files=[file])
        docker_client.compose.down()


def compose_files_up():
    compose_file_paths: list[str] = get_compose_file_paths()

    for file in compose_file_paths:
        if not file_exists(file):
            continue
        docker_client = DockerClient(compose_files=[file])
        docker_client.compose.up(detach=True)


def get_containers_list(show_all: bool = True) -> list[Container]:
    containers = docker.container.list(all=show_all)
    return containers
