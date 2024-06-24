import psutil
import GPUtil
from tabulate import tabulate
import time

def get_gpu_info():
    gpus = GPUtil.getGPUs()
    gpu_list = []
    for gpu in gpus:
        gpu_info = {
            "GPU": gpu.name,
            "Load (%)": f"{gpu.load * 100:.2f}",
            "Memory Used (MB)": f"{gpu.memoryUsed:.2f}",
            "Memory Total (MB)": f"{gpu.memoryTotal:.2f}",
            "Temperature (C)": f"{gpu.temperature:.2f}",
        }
        gpu_list.append(gpu_info)
    return gpu_list

def print_gpu_info():
    gpu_info = get_gpu_info()
    if gpu_info:
        print(tabulate(gpu_info, headers="keys"))
    else:
        print("No GPU found.")

if __name__ == "__main__":
    while True:
        print("\n" + "="*30 + " GPU Usage " + "="*30)
        print_gpu_info()
        time.sleep(5)
