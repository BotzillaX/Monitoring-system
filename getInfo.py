import psutil

def ramUsage():
    virtual_memory = psutil.virtual_memory()

    total_memory = virtual_memory.total / (1024 ** 3)  # Convert to GB
    available_memory = virtual_memory.available / (1024 ** 3)  # Convert to GB
    used_memory = virtual_memory.used / (1024 ** 3)  # Convert to GB
    memory_percentage = virtual_memory.percent
    
    print("Total Memory: " + str(round(total_memory, 2)) + " GB")
    print("Available Memory: " + str(round(available_memory, 2)) + " GB")
    print("Used Memory: " + str(round(used_memory, 2)) + " GB")
    print("Memory Usage Percentage: " + str(memory_percentage) + "%")

    return total_memory, available_memory, used_memory, memory_percentage

if __name__ == "__main__":
    total_memory, available_memory, used_memory, memory_percentage = ramUsage()
