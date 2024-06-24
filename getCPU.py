import psutil
import time

def cpuUsage():
    cpu_usage = psutil.cpu_percent()
    print(f"CPU Usage: {cpu_usage}%")



