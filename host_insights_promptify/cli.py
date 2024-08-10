import argparse
from host_insights_promptify import gather_all_insights, collect_system_info, collect_network_info, collect_docker_info, collect_services_info, save_prompt_to_file

def main():
    parser = argparse.ArgumentParser(description="Host-Insights-Promptify: A tool for gathering and optimizing system insights into an AI-ready prompt.")
    
    parser.add_argument("--all", action="store_true", help="Collect all information and format it into an AI-ready prompt")
    parser.add_argument("--system", action="store_true", help="Collect system-related information only")
    parser.add_argument("--network", action="store_true", help="Collect network-related information only")
    parser.add_argument("--docker", action="store_true", help="Collect Docker-related information only")
    parser.add_argument("--services", action="store_true", help="Collect information about running services only")
    parser.add_argument("--output", type=str, help="Specify a file to save the output")

    args = parser.parse_args()

    if args.all or not any(vars(args).values()):
        # If --all is specified or no specific option is given, gather all insights
        try:
            prompt = gather_all_insights()
            if args.output:
                save_prompt_to_file(prompt, args.output)
            else:
                print(prompt)
        except Exception as e:
            print(f"Error gathering all insights: {str(e)}")
    elif args.system:
        try:
            system_info = collect_system_info()
            if args.output:
                save_prompt_to_file(system_info, args.output)
            else:
                print(system_info)
        except Exception as e:
            print(f"Error gathering system information: {str(e)}")
    elif args.network:
        try:
            network_info = collect_network_info()
            if args.output:
                save_prompt_to_file(network_info, args.output)
            else:
                print(network_info)
        except Exception as e:
            print(f"Error gathering network information: {str(e)}")
    elif args.docker:
        try:
            docker_info = collect_docker_info()
            if args.output:
                save_prompt_to_file(docker_info, args.output)
            else:
                print(docker_info)
        except Exception as e:
            print(f"Error gathering Docker information: {str(e)}")
    elif args.services:
        try:
            services_info = collect_services_info()
            if args.output:
                save_prompt_to_file(services_info, args.output)
            else:
                print(services_info)
        except Exception as e:
            print(f"Error gathering services information: {str(e)}")

if __name__ == "__main__":
    main()