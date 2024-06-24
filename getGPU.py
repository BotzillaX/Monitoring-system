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
        return gpu_load
    else:
        print("No GPU found.")

if __name__ == "__main__":

    print(str(print_gpu_load())+ "%")
    