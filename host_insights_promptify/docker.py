import docker

def collect_docker_info():
    """
    Collects detailed information about Docker containers, networks, and volumes.

    Returns:
        dict: A dictionary containing Docker information such as running containers, networks, and volumes.
    """
    client = docker.from_env()
    docker_info = {
        "containers": [],
        "networks": [],
        "volumes": []
    }

    try:
        # Collect running containers with detailed info
        containers = client.containers.list()
        for container in containers:
            try:
                container_stats = container.stats(stream=False)
                cpu_usage = container_stats["cpu_stats"]["cpu_usage"]["total_usage"]
                memory_usage = container_stats["memory_stats"]["usage"]
            except KeyError:
                # Handle the case where stats might not be available or complete
                cpu_usage = "N/A"
                memory_usage = "N/A"

            docker_info["containers"].append({
                "name": container.name,
                "image": container.image.tags,
                "status": container.status,
                "ports": container.ports,
                "cpu_usage": cpu_usage,
                "memory_usage": memory_usage,
                "env": container.attrs["Config"]["Env"],
                "health_status": container.attrs["State"].get("Health", {}).get("Status", "No health check"),
                "restart_policy": container.attrs["HostConfig"]["RestartPolicy"]["Name"],
                "mounts": container.attrs["Mounts"],
                "networks": container.attrs["NetworkSettings"]["Networks"]
            })

        # Collect networks with detailed info
        networks = client.networks.list()
        for network in networks:
            docker_info["networks"].append({
                "name": network.name,
                "id": network.id,
                "driver": network.attrs["Driver"],
                "subnet": network.attrs["IPAM"]["Config"][0].get("Subnet"),
                "gateway": network.attrs["IPAM"]["Config"][0].get("Gateway"),
                "containers": list(network.containers)
            })

        # Collect volumes with detailed info
        volumes = client.volumes.list()
        for volume in volumes:
            docker_info["volumes"].append({
                "name": volume.name,
                "mountpoint": volume.attrs['Mountpoint'],
                "driver": volume.attrs["Driver"],
                "labels": volume.attrs.get("Labels", {}),
                # Docker API does not provide direct usage statistics for volumes,
                # so usage statistics are not included here.
            })

    except docker.errors.APIError as e:
        docker_info["error"] = f"Error collecting Docker information: {str(e)}"
    except Exception as e:
        docker_info["error"] = f"Unexpected error: {str(e)}"

    return docker_info