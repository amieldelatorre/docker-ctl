class Service:
    service_name: str
    container_name: str
    container_status: str
    
    def __init__(self, service_name: str, container_name: str, container_status: str):
        self.service_name = service_name
        self.container_name = container_name
        self.container_status = container_status
