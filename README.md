# Host-Insights-Promptify

Host-Insights-Promptify is a cross-platform command-line tool designed to gather detailed insights about a host system. Whether you're troubleshooting, optimizing, or preparing for technical support, Host-Insights-Promptify provides comprehensive information to help you understand your system's state and environment.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Cross-Platform Compatibility**: Runs on Linux, macOS, and Windows.
- **Modular Design**: Collects various types of information, including system, network, Docker, services, and more.
- **Comprehensive Insights**: Gathers system configuration, network settings, Docker container details, running services, scheduled tasks, and more.
- **Easy to Use**: Simple command-line interface with options for specific or comprehensive data collection.
- **Open Source**: Licensed under the GNU General Public License v3.0 (GPLv3), ensuring that all modifications and derivatives remain open source.

## Installation

### Prerequisites

- **Python 3.x**: Host-Insights-Promptify is written in Python, so you'll need Python 3.x installed on your system.
- **Dependencies**: The necessary Python dependencies can be installed via `pip3`.

### Installation Steps

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yoclaire/host-insights-promptify.git
    cd host-insights-promptify
    ```

2. **Install Dependencies**:
    - Use `pip3` to ensure you're installing the dependencies for Python 3.x:
    ```bash
    pip3 install -r requirements.txt
    ```

3. **Make the Tool Globally Accessible** (optional):
    ```bash
    python3 setup.py install
    ```

## Usage

Host-Insights-Promptify provides a command-line interface (CLI) for gathering various types of system information. By default, running the tool without any options will gather all available information.

### Basic Usage

- **Default Usage**:
    ```bash
    host-insights-promptify
    ```

- **Explicitly Collect All Information**:
    ```bash
    host-insights-promptify --all
    ```

- **Collect System Information**:
    ```bash
    host-insights-promptify --system
    ```

- **Collect Network Information**:
    ```bash
    host-insights-promptify --network
    ```

- **Collect Docker Information**:
    ```bash
    host-insights-promptify --docker
    ```

### Options

- `--all`: Gather all available information.
- `--system`: Gather system-related information (OS, memory, disk usage, etc.).
- `--network`: Gather network-related information (interfaces, routing table, etc.).
- `--docker`: Gather Docker-related information (containers, networks, volumes, etc.).
- `--services`: Gather information about running services.
- `--cron`: Gather scheduled cron jobs.
- `--help`: Display help message and usage details.

## Examples

- **Gather Comprehensive Host Information**:
    ```bash
    host-insights-promptify --all
    ```

- **Gather Docker-Specific Information**:
    ```bash
    host-insights-promptify --docker
    ```

- **Gather System Information**:
    ```bash
    host-insights-promptify --system
    ```

## Contributing

We welcome contributions to Host-Insights-Promptify! Whether you're fixing bugs, adding new features, or improving documentation, your help is greatly appreciated.

### How to Contribute

1. **Fork the Repository**: Click the "Fork" button at the top-right of the repository page.
2. **Clone Your Fork**:
    ```bash
    git clone https://github.com/[yourusername]/host-insights-promptify.git
    ```
3. **Create a New Branch**:
    ```bash
    git checkout -b feature/your-feature-name
    ```
4. **Make Your Changes**: Implement your changes or new features.
5. **Commit Your Changes**:
    ```bash
    git add .
    git commit -m "Add feature: your-feature-name"
    ```
6. **Push to Your Fork**:
    ```bash
    git push origin feature/your-feature-name
    ```
7. **Submit a Pull Request**: Go to the repository in your GitHub account and submit a pull request.

### Branch Naming Convention

- **Feature Branches**: `feature/<short-description>`
- **Bugfix Branches**: `bugfix/<issue-id>-<short-description>`
- **Hotfix Branches**: `hotfix/<short-description>`
- **Release Branches**: `release/<version>`
- **Documentation Branches**: `docs/<short-description>`

## License

Host-Insights-Promptify is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for more details.

---

**Hack the Planet!**
