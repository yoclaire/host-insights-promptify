"""
Host-Insights-Promptify
========================
A utility for gathering and optimizing system insights into a single, AI-ready prompt.

This package provides modules for collecting various types of system information, including
system specifications, network configurations, Docker container statuses, and running services.
The core functionality is focused on processing this data into a concise, structured format
suitable for AI-based analysis and interaction.

Modules:
--------
- system: Handles system-level information gathering.
- network: Manages network interface and routing details.
- docker: Collects data on Docker containers, networks, and volumes.
- services: Retrieves information about running services on the host.
- promptify: Processes and formats the gathered data into an AI-ready prompt.

Core Function:
--------------
- gather_all_insights: Collects all insights and formats them into a single AI-ready prompt.
"""

from .system import collect_system_info
from .network import collect_network_info
from .docker import collect_docker_info
from .services import collect_services_info
from .promptify import format_prompt

__all__ = [
    "collect_system_info",
    "collect_network_info",
    "collect_docker_info",
    "collect_services_info",
    "format_prompt",
    "gather_all_insights",
]

__version__ = "0.1.0"
__author__ = "Your Name"
__license__ = "GPLv3"

def gather_all_insights():
    """
    Gathers all system insights and formats them into an AI-ready prompt.

    Returns:
        str: A formatted prompt containing all relevant system insights.
    """
    system_info = collect_system_info()
    network_info = collect_network_info()
    docker_info = collect_docker_info()
    services_info = collect_services_info()

    # Format the collected data into a single AI-ready prompt
    return format_prompt(system_info, network_info, docker_info, services_info)