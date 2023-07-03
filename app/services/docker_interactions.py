import json
from app.models.service import Service
from app.services.os_interactions import get_compose_file_paths
from app.utils.compose_file_list import check_file_exists
from python_on_whales import DockerClient, docker
from pathlib import Path
from os.path import basename

def get_compose_files_info() -> dict[str, list[Service]]:
    compose_file_paths: list[str] = get_compose_file_paths()

    compose_files_and_services_info: dict[str, list[Service]] = {}
    for compose_file_path in compose_file_paths:
        compose_file_dir = basename(Path(compose_file_path).parent)

        compose_files_and_services_info[compose_file_dir] = get_services_info(compose_file_path)

    return compose_files_and_services_info

def get_services_info(compose_file_path: str) -> list[Service]:
    if not check_file_exists(compose_file_path):
        return None
    
    services: dict[str, str] = get_services_for_compose(compose_file_path)
    services_info: list[Service] = []
    for service_name in services.keys():
        info: Service = get_service(service_name=service_name, container_name=services[service_name])
        services_info.append(info)

    return services_info

def get_services_for_compose(compose_file_path: str) -> dict[str, str]:
    docker_client = DockerClient(compose_files=[compose_file_path])
    compose_config = docker_client.compose.config(return_json=True)
    services_config = compose_config["services"]

    services: dict[str, str] = {}
    for name in services_config.keys():
        services[name] = services_config[name]["container_name"]
    
    return services

def get_service(service_name: str, container_name: str) -> Service:
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
        if not check_file_exists(file):
            continue
        docker_client = DockerClient(compose_files=[file])
        docker_client.compose.down()

def compose_files_up():
    compose_file_paths: list[str] = get_compose_file_paths()

    for file in compose_file_paths:
        if not check_file_exists(file):
            continue
        docker_client = DockerClient(compose_files=[file])
        docker_client.compose.up(detach=True)