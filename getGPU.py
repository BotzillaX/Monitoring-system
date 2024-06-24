import subprocess
import time

try:
    import pynvml
    NVML_AVAILABLE = True
except ImportError:
    NVML_AVAILABLE = False

def initialize_nvml():
    try:
        pynvml.nvmlInit()
    except pynvml.NVMLError as error:
        print(f"Failed to initialize NVML: {error}")
        return False
    return True

def get_nvidia_gpu_usage():
    try:
        device_count = pynvml.nvmlDeviceGetCount()
        for i in range(device_count):
            handle = pynvml.nvmlDeviceGetHandleByIndex(i)
            gpu_name = pynvml.nvmlDeviceGetName(handle)
            gpu_usage = pynvml.nvmlDeviceGetUtilizationRates(handle)
            memory_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
            print(f"NVIDIA GPU {i} - {gpu_name.decode('utf-8')}")
            print(f"  GPU Usage: {gpu_usage.gpu}%")
            print(f"  Memory Usage: {memory_info.used / 1024**2:.2f} MiB / {memory_info.total / 1024**2:.2f} MiB")
    except pynvml.NVMLError as error:
        print(f"Failed to get NVIDIA GPU usage: {error}")

def get_amd_gpu_usage():
    try:
        result = subprocess.run(['rocm-smi', '--showuse'], capture_output=True, text=True)
        print("AMD GPU Usage:\n", result.stdout)
    except FileNotFoundError:
        print("rocm-smi not found. Please install the ROCm tools.")

def main():
    if NVML_AVAILABLE:
        if not initialize_nvml():
            return

    try:
        while True:
            if NVML_AVAILABLE:
                get_nvidia_gpu_usage()
            get_amd_gpu_usage()
            time.sleep(5)  # Refresh every 5 seconds
    except KeyboardInterrupt:
        print("Monitoring stopped.")
    finally:
        if NVML_AVAILABLE:
            pynvml.nvmlShutdown()

if __name__ == "__main__":
    main()
