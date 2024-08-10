import argparse
from host_insights_promptify import gather_all_insights, collect_system_info, collect_network_info, collect_docker_info, collect_services_info

def main():
    parser = argparse.ArgumentParser(description="Host-Insights-Promptify: A tool for gathering and optimizing system insights into an AI-ready prompt.")
    
    parser.add_argument("--all", action="store_true", help="Collect all information and format it into an AI-ready prompt")
    parser.add_argument("--system", action="store_true", help="Collect system-related information only")
    parser.add_argument("--network", action="store_true", help="Collect network-related information only")
    parser.add_argument("--docker", action="store_true", help="Collect Docker-related information only")
    parser.add_argument("--services", action="store_true", help="Collect information about running services only")

    args = parser.parse_args()

    if args.all or not any(vars(args).values()):
        # If --all is specified or no specific option is given, gather all insights
        prompt = gather_all_insights()
        print(prompt)
    elif args.system:
        # Collect and print system information
        system_info = collect_system_info()
        print(system_info)
    elif args.network:
        # Collect and print network information
        network_info = collect_network_info()
        print(network_info)
    elif args.docker:
        # Collect and print Docker information
        docker_info = collect_docker_info()
        print(docker_info)
    elif args.services:
        # Collect and print services information
        services_info = collect_services_info()
        print(services_info)

if __name__ == "__main__":
    main()