import argparse
import json
import psutil
from src.monitor import Monitor
from src.utils import parse_config

def main():
    parser = argparse.ArgumentParser(description='System Resource Monitoring Tool')
    parser.add_argument('--config', help='Path to configuration file')
    parser.add_argument('--start', action='store_true', help='Start monitoring')
    parser.add_argument('--stats', action='store_true', help='View system resource utilization')
    args = parser.parse_args()

    if args.config:
        config = parse_config(args.config)
    else:
        config = {}

    if args.start:
        monitor = Monitor(config)
        monitor.start()
    elif args.stats:
        monitor = Monitor(config)
        print(monitor.get_stats())

if __name__ == '__main__':
    main()