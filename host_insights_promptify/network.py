import psutil
import socket
import subprocess
import platform

def collect_network_info():
    """
    Collects detailed information about network interfaces, routing tables, active connections, 
    DNS configuration, and firewall rules.

    Returns:
        dict: A dictionary containing network-related information.
    """
    network_info = {
        "interfaces": [],
        "routing_table": [],
        "active_connections": [],
        "dns": {},
        "firewall_rules": None
    }

    try:
        # Collect network interfaces and their details
        for interface_name, addrs in psutil.net_if_addrs().items():
            interface_info = {
                "name": interface_name,
                "ipv4": None,
                "ipv6": None,
                "mac": None,
                "netmask": None,
                "broadcast": None,
                "mtu": None,
                "status": "up" if psutil.net_if_stats()[interface_name].isup else "down",
                "speed": psutil.net_if_stats()[interface_name].speed
            }
            for addr in addrs:
                if addr.family == socket.AF_INET:
                    interface_info["ipv4"] = addr.address
                    interface_info["netmask"] = addr.netmask
                    interface_info["broadcast"] = addr.broadcast
                elif addr.family == socket.AF_INET6:
                    interface_info["ipv6"] = addr.address
                elif addr.family == psutil.AF_LINK:
                    interface_info["mac"] = addr.address
            network_info["interfaces"].append(interface_info)

        # Collect routing table
        routes = psutil.net_if_stats().items()
        for route in psutil.net_if_stats().keys():
            route_info = {
                "destination": route,
                "gateway": psutil.net_if_addrs()[route][0].address,
                "interface": psutil.net_if_stats()[route].isup,
                "netmask": psutil.net_if_addrs()[route][0].netmask,
                "flags": "U" if psutil.net_if_stats()[route].isup else "",
                "metric": psutil.net_if_stats()[route].speed
            }
            network_info["routing_table"].append(route_info)

        # Collect active connections
        connections = psutil.net_connections()
        for conn in connections:
            connection_info = {
                "protocol": "TCP" if conn.type == socket.SOCK_STREAM else "UDP",
                "local_address": f"{conn.laddr.ip}:{conn.laddr.port}",
                "remote_address": f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else None,
                "status": conn.status,
                "pid": conn.pid,
                "process": psutil.Process(conn.pid).name() if conn.pid else None
            }
            network_info["active_connections"].append(connection_info)

        # Collect DNS configuration
        if platform.system() == "Linux":
            with open('/etc/resolv.conf', 'r') as f:
                lines = f.readlines()
                for line in lines:
                    if line.startswith('nameserver'):
                        dns_server = line.split()[1]
                        if "primary" not in network_info["dns"]:
                            network_info["dns"]["primary"] = dns_server
                        else:
                            network_info["dns"]["secondary"] = dns_server
                    elif line.startswith('search'):
                        network_info["dns"]["search_domains"] = line.split()[1:]

        elif platform.system() == "Darwin":  # macOS
            result = subprocess.run(['scutil', '--dns'], capture_output=True, text=True)
            dns_output = result.stdout.splitlines()
            for line in dns_output:
                if 'nameserver' in line:
                    dns_server = line.split()[-1]
                    if "primary" not in network_info["dns"]:
                        network_info["dns"]["primary"] = dns_server
                    else:
                        network_info["dns"]["secondary"] = dns_server
                elif 'search domain' in line:
                    if "search_domains" not in network_info["dns"]:
                        network_info["dns"]["search_domains"] = []
                    network_info["dns"]["search_domains"].append(line.split()[-1])

        # Collect firewall rules (assuming iptables on Linux)
        if platform.system() == "Linux":
            result = subprocess.run(['iptables', '-L'], capture_output=True, text=True)
            network_info["firewall_rules"] = result.stdout

        elif platform.system() == "Darwin":  # macOS
            result = subprocess.run(['sudo', 'pfctl', '-sr'], capture_output=True, text=True)
            network_info["firewall_rules"] = result.stdout

    except Exception as e:
        network_info["error"] = f"Error collecting network information: {str(e)}"

    return network_info