import psutil
from datetime import datetime

def collect_services_info():
    """
    Collects information about running services on the system.

    Returns:
        list: A list of dictionaries, each containing details about a running service.
    """
    services_info = []

    try:
        for process in psutil.process_iter(['pid', 'name', 'status', 'create_time', 'memory_info', 'cpu_percent']):
            try:
                service_info = {
                    'name': process.info['name'],
                    'status': process.info['status'],
                    'start_time': datetime.fromtimestamp(process.info['create_time']).strftime("%Y-%m-%d %H:%M:%S"),
                    'memory_usage': process.info['memory_info'].rss if process.info['memory_info'] else 'N/A',  # Resident Set Size
                    'cpu_usage': process.info['cpu_percent'] if process.info['cpu_percent'] else 'N/A'
                }
                services_info.append(service_info)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
                # Log or handle the error, but don't append it to the services info
                print(f"Error processing service: {e}")

    except Exception as e:
        # General error handling if psutil.process_iter fails
        print(f"Error collecting service information: {str(e)}")

    return services_info