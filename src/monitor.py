import psutil
import time

class Monitor:
    def __init__(self, config):
        self.config = config
        self.interval = config.get('interval', 10)
        self.thresholds = config.get('thresholds', {})

    def start(self):
        while True:
            self.collect_data()
            time.sleep(self.interval)

    def collect_data(self):
        cpu_util = psutil.cpu_percent()
        mem_util = psutil.virtual_memory().percent
        # Add more monitoring metrics as needed

        # Alert if thresholds are exceeded
        if cpu_util > self.thresholds.get('cpu', 80):
            print(f'CPU utilization exceeded threshold: {cpu_util}%')
        if mem_util > self.thresholds.get('mem', 80):
            print(f'Memory utilization exceeded threshold: {mem_util}%')