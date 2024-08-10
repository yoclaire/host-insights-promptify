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
            "CPU Frequency": f"{psutil.cpu_freq().current:.2f} MHz" if psutil.cpu_freq() else "N/A",
            "Total Memory": f"{psutil.virtual_memory().total / (1024 ** 3):.2f} GB",
            "Available Memory": f"{psutil.virtual_memory().available / (1024 ** 3):.2f} GB",
            "Disk": f"{psutil.disk_usage('/').total / (1024 ** 3):.2f} GB",
            "Disk Available": f"{psutil.disk_usage('/').free / (1024 ** 3):.2f} GB",
            "Disk Usage": f"{psutil.disk_usage('/').percent}%"
        }

        # Collect disk information for all partitions
        partitions_info = []
        partitions = psutil.disk_partitions()
        for partition in partitions:
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
        system_info["Disk Partitions"] = partitions_info

    except Exception as e:
        system_info = {"error": f"Error collecting system information: {str(e)}"}

    return system_info