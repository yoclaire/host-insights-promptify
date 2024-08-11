import platform
import psutil

def collect_system_info():
    """
    Collects information about the system's hardware and operating system.

    Returns:
        dict: A dictionary containing system-related information such as OS, CPU, memory, and disk usage.
    """
    try:
        system_info = {
            "OS": platform.system(),
            "OS Version": platform.version(),
            "Architecture": platform.architecture()[0],
            "Hostname": platform.node(),
            "CPU": platform.processor(),
            "Physical Cores": psutil.cpu_count(logical=False),
            "Logical Cores": psutil.cpu_count(logical=True),
            "CPU Frequency": "N/A",  # Default to "N/A" if the frequency can't be retrieved
            "Total Memory": "N/A",  # Default to "N/A" if memory info can't be retrieved
            "Available Memory": "N/A",  # Default to "N/A" if memory info can't be retrieved
            "Disk": "N/A",  # Default to "N/A" if disk info can't be retrieved
            "Disk Available": "N/A",  # Default to "N/A" if disk info can't be retrieved
            "Disk Usage": "N/A",  # Default to "N/A" if disk usage can't be retrieved
            "Disk Partitions": []  # Initialize as empty list
        }

        # Attempt to get the CPU frequency, but handle the case where it fails
        try:
            cpu_freq = psutil.cpu_freq()
            if cpu_freq:
                system_info["CPU Frequency"] = f"{cpu_freq.current:.2f} MHz"
        except Exception as e:
            system_info["CPU Frequency"] = "N/A"

        # Attempt to get memory information
        try:
            memory_info = psutil.virtual_memory()
            system_info["Total Memory"] = f"{memory_info.total / (1024 ** 3):.2f} GB"
            system_info["Available Memory"] = f"{memory_info.available / (1024 ** 3):.2f} GB"
        except Exception as e:
            system_info["Total Memory"] = "N/A"
            system_info["Available Memory"] = "N/A"

        # Attempt to get disk information
        try:
            disk_usage = psutil.disk_usage('/')
            system_info["Disk"] = f"{disk_usage.total / (1024 ** 3):.2f} GB"
            system_info["Disk Available"] = f"{disk_usage.free / (1024 ** 3):.2f} GB"
            system_info["Disk Usage"] = f"{disk_usage.percent}%"
        except Exception as e:
            system_info["Disk"] = "N/A"
            system_info["Disk Available"] = "N/A"
            system_info["Disk Usage"] = "N/A"

        # Collect disk partition information
        partitions_info = []
        partitions = psutil.disk_partitions()
        for partition in partitions:
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
                partitions_info.append({
                    "Device": partition.device,
                    "Mountpoint": partition.mountpoint,
                    "File System": partition.fstype,
                    "Total Size": f"{partition_usage.total / (1024 ** 3):.2f} GB",
                    "Used": f"{partition_usage.used / (1024 ** 3):.2f} GB",
                    "Free": f"{partition_usage.free / (1024 ** 3):.2f} GB",
                    "Usage": f"{partition_usage.percent}%"
                })
            except PermissionError:
                # Skip partitions where permission is denied
                continue
            except Exception as e:
                # Handle other potential exceptions with disk partitions
                continue
        
        system_info["Disk Partitions"] = partitions_info

    except Exception as e:
        system_info = {"error": f"Error collecting system information: {str(e)}"}

    return system_info