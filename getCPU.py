import psutil
import time

def cpuUsage():
    cpu_usage = psutil.cpu_percent()
    #print(f"CPU Usage: {cpu_usage}%")
    return cpu_usage

if __name__ == "__main__":
    cpuUsage()



