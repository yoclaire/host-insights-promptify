import platform
import psutil

def collect_system_info():
    """
    Collects information about the system's hardware and operating system.

    Returns:
        dict: A dictionary containing system-related information such as OS, CPU, memory, and disk usage.
    """
    system_info = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Architecture": platform.architecture()[0],
        "Hostname": platform.node(),
        "CPU": platform.processor(),
        "Memory": f"{psutil.virtual_memory().total / (1024 ** 3):.2f} GB",
        "Disk": f"{psutil.disk_usage('/').total / (1024 ** 3):.2f} GB"
    }

    return system_info