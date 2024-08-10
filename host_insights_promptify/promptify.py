import os

def format_prompt(system_info, network_info, docker_info, services_info):
    """
    Formats the collected system, network, Docker, and services information into a single AI-ready prompt.

    Args:
        system_info (dict): System-related information.
        network_info (dict): Network-related information.
        docker_info (dict): Docker-related information.
        services_info (dict): Information about running services.

    Returns:
        str: A formatted string containing all the collected information, optimized for AI interaction.
    """
    prompt = []

    # Header with directives
    prompt.append("### AI SYSTEM INSIGHTS REPORT ###")
    prompt.append("This report provides a detailed overview of the current system's state. Your task is to use this information to assist with any queries or issues related to the system. Please keep the following in mind:")
    prompt.append("- Be proactive in identifying potential issues or optimizations based on the data provided.")
    prompt.append("- Always search the web for additional, up-to-date information if needed to ensure that the advice provided is accurate and current.")
    prompt.append("- Ensure all recommendations adhere to the latest security best practices and are tailored to the specific configurations of this system.")
    prompt.append("- Verify the correctness of all information before making suggestions or changes.")
    prompt.append("- Offer specific suggestions and advice on how to address any concerns that might arise from the system's current state.")
    prompt.append("- Be prepared to answer follow-up questions with additional details or clarifications as needed.")
    prompt.append("")

    # System Information
    prompt.append("### Section 1: System Information ###")
    prompt.append("The following data provides an overview of the system's hardware and operating system:")
    prompt.append(f"- Operating System: {system_info.get('OS', 'N/A')}")
    prompt.append(f"- OS Version: {system_info.get('OS Version', 'N/A')}")
    prompt.append(f"- Architecture: {system_info.get('Architecture', 'N/A')}")
    prompt.append(f"- Hostname: {system_info.get('Hostname', 'N/A')}")
    prompt.append(f"- CPU: {system_info.get('CPU', 'N/A')}")
    prompt.append(f"- Memory: {system_info.get('Memory', 'N/A')}")
    prompt.append(f"- Disk: {system_info.get('Disk', 'N/A')}")
    prompt.append("")
    prompt.append("Review this information to ensure the system is running optimally. If any configurations seem suboptimal, provide recommendations.")
    prompt.append("")

    # Network Information
    prompt.append("### Section 2: Network Information ###")
    prompt.append("Details regarding network interfaces, routing, active connections, DNS configuration, and firewall rules:")
    
    prompt.append("#### 2.1 Network Interfaces ####")
    for iface in network_info.get('interfaces', []):
        prompt.append(f"- Interface: {iface.get('name', 'N/A')}")
        prompt.append(f"  - Status: {iface.get('status', 'N/A')}")
        prompt.append(f"  - IPv4 Address: {iface.get('ipv4', 'N/A')}")
        prompt.append(f"  - IPv6 Address: {iface.get('ipv6', 'N/A')}")
        prompt.append(f"  - MAC Address: {iface.get('mac', 'N/A')}")
        prompt.append(f"  - Netmask: {iface.get('netmask', 'N/A')}")
        prompt.append(f"  - Broadcast: {iface.get('broadcast', 'N/A')}")
        prompt.append(f"  - MTU: {iface.get('mtu', 'N/A')}")
        prompt.append(f"  - Speed: {iface.get('speed', 'N/A')} Mbps")
        prompt.append("")
    prompt.append("Check the status and configurations of the network interfaces. Provide guidance if any interfaces are down or misconfigured.")
    prompt.append("")
    
    prompt.append("#### 2.2 Routing Table ####")
    for route in network_info.get('routing_table', []):
        prompt.append(f"- Destination: {route.get('destination', 'N/A')}")
        prompt.append(f"  - Gateway: {route.get('gateway', 'N/A')}")
        prompt.append(f"  - Interface: {route.get('interface', 'N/A')}")
        prompt.append(f"  - Netmask: {route.get('netmask', 'N/A')}")
        prompt.append(f"  - Flags: {route.get('flags', 'N/A')}")
        prompt.append(f"  - Metric: {route.get('metric', 'N/A')}")
        prompt.append("")
    prompt.append("Analyze the routing table for any potential misconfigurations or routes that might affect network performance. Offer insights on improving routing efficiency.")
    prompt.append("")

    prompt.append("#### 2.3 Active Connections ####")
    for conn in network_info.get('active_connections', []):
        prompt.append(f"- Protocol: {conn.get('protocol', 'N/A')}")
        prompt.append(f"  - Local Address: {conn.get('local_address', 'N/A')}")
        prompt.append(f"  - Remote Address: {conn.get('remote_address', 'N/A')}")
        prompt.append(f"  - Status: {conn.get('status', 'N/A')}")
        prompt.append(f"  - Associated Process: {conn.get('process', 'N/A')} (PID: {conn.get('pid', 'N/A')})")
        prompt.append("")
    prompt.append("Review active connections to ensure there are no unauthorized or suspicious activities. Provide advice on securing network traffic where necessary.")
    prompt.append("")

    prompt.append("#### 2.4 DNS Configuration ####")
    prompt.append(f"- Primary DNS: {network_info['dns'].get('primary', 'N/A')}")
    prompt.append(f"- Secondary DNS: {network_info['dns'].get('secondary', 'N/A')}")
    prompt.append(f"- Search Domains: {', '.join(network_info['dns'].get('search_domains', []))}")
    prompt.append("")
    prompt.append("Evaluate the DNS settings. Suggest improvements if the current configuration might cause resolution delays or other issues.")
    prompt.append("")

    if network_info.get('firewall_rules'):
        prompt.append("#### 2.5 Firewall Rules ####")
        prompt.append(network_info['firewall_rules'])
        prompt.append("")
    prompt.append("Check the firewall rules for any gaps in security. Recommend changes to tighten security if necessary.")
    prompt.append("")

    # Docker Information
    if docker_info["containers"] or docker_info["networks"] or docker_info["volumes"]:
        prompt.append("### Section 3: Docker Information ###")
        prompt.append("Information about Docker containers, networks, and volumes on the system:")
        
        prompt.append("#### 3.1 Containers ####")
        for container in docker_info.get("containers", []):
            prompt.append(f"- Container Name: {container.get('name', 'N/A')}")
            prompt.append(f"  - Image: {', '.join(container.get('image', []))}")
            prompt.append(f"  - Status: {container.get('status', 'N/A')}")
            prompt.append(f"  - Ports: {container.get('ports', 'N/A')}")
            prompt.append(f"  - CPU Usage: {container.get('cpu_usage', 'N/A')}")
            prompt.append(f"  - Memory Usage: {container.get('memory_usage', 'N/A')} bytes")
            prompt.append(f"  - Health Status: {container.get('health_status', 'N/A')}")
            prompt.append(f"  - Restart Policy: {container.get('restart_policy', 'N/A')}")
            prompt.append(f"  - Mounts: {container.get('mounts', 'N/A')}")
            prompt.append(f"  - Networks: {container.get('networks', 'N/A')}")
            prompt.append("")
        prompt.append("Examine the state of Docker containers. If any containers are underperforming or experiencing issues, suggest troubleshooting steps or optimizations.")
        prompt.append("")

        prompt.append("#### 3.2 Networks ####")
        for network in docker_info.get("networks", []):
            prompt.append(f"- Network Name: {network.get('name', 'N/A')}")
            prompt.append(f"  - ID: {network.get('id', 'N/A')}")
            prompt.append(f"  - Driver: {network.get('driver', 'N/A')}")
            prompt.append(f"  - Subnet: {network.get('subnet', 'N/A')}")
            prompt.append(f"  - Gateway: {network.get('gateway', 'N/A')}")
            prompt.append(f"  - Connected Containers: {', '.join([container for container in network.get('containers', [])])}")
            prompt.append("")
        prompt.append("Assess the Docker network configurations. Provide recommendations if there are any security or performance concerns.")
        prompt.append("")

        prompt.append("#### 3.3 Volumes ####")
        for volume in docker_info.get("volumes", []):
            prompt.append(f"- Volume Name: {volume.get('name', 'N/A')}")
            prompt.append(f"  - Mountpoint: {volume.get('mountpoint', 'N/A')}")
            prompt.append(f"  - Driver: {volume.get('driver', 'N/A')}")
            prompt.append(f"  - Labels: {volume.get('labels', 'N/A')}")
            prompt.append("")
        prompt.append("Review Docker volumes. If there are storage or access issues, offer potential solutions.")
        prompt.append("")

    # Services Information
    if services_info:
        prompt.append("### Section 4: Running Services ###")
        prompt.append("The following services are currently running on the system:")
        for service in services_info:
            prompt.append(f"- Service Name: {service.get('name', 'N/A')}")
            prompt.append(f"  - Status: {service.get('status', 'N/A')}")
            prompt.append(f"  - Start Time: {service.get('start_time', 'N/A')}")
            prompt.append(f"  - Memory Usage: {service.get('memory_usage', 'N/A')} bytes")
            prompt.append(f"  - CPU Usage: {service.get('cpu_usage', 'N/A')}")
            prompt.append("")
        prompt.append("Ensure that all critical services are running as expected. If any services are misbehaving or consuming excessive resources, suggest corrective actions.")
        prompt.append("")

    # Closing statement
    prompt.append("### END OF REPORT ###")
    prompt.append("Please ensure that all suggestions are verified and are in line with the latest security best practices. Be prepared to provide further assistance and clarification as needed.")
    
    return "\n".join(prompt)

def save_prompt_to_file(prompt, file_path="host_insights_prompt.txt"):
    """
    Saves the generated prompt to a file.

    Args:
        prompt (str): The generated AI-ready prompt.
        file_path (str): The file path where the prompt will be saved.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(prompt)
        print(f"Prompt saved to {file_path}")
    except Exception as e:
        print(f"Error saving prompt to {file_path}: {str(e)}")