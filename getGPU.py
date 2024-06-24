import GPUtil
import time

def get_gpu_load():
    gpus = GPUtil.getGPUs()
    if gpus:
        gpu_load = gpus[0].load * 100
        return gpu_load
    else:
        return None

def print_gpu_load():
    gpu_load = get_gpu_load()
    if gpu_load is not None:
        print(f"Current GPU Load: {gpu_load:.2f}%")
    else:
        print("No GPU found.")

if __name__ == "__main__":
    while True:
        print("\n" + "="*30 + " GPU Usage " + "="*30)
        print_gpu_load()
        time.sleep(1)  # Sleep for 1 second before printing the next reading
