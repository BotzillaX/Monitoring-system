import psutil
import wmi

def ramUsage():
    
    virtual_memory = psutil.virtual_memory()

    total_memory = virtual_memory.total / (1024 ** 3)  # Convert to GB
    available_memory = virtual_memory.available / (1024 ** 3)  # Convert to GB
    used_memory = virtual_memory.used / (1024 ** 3)  # Convert to GB
    memory_percentage = virtual_memory.percent

    #print("Total Memory: " + str(round(total_memory, 2)) + " GB")
    #print("Available Memory: " + str(round(available_memory, 2)) + " GB")
    #print("Used Memory: " + str(round(used_memory, 2)) + " GB")
    #print("Memory Usage Percentage: " + str(memory_percentage) + "%")
    temperature = getRamTemperature()
    return total_memory, available_memory, used_memory, memory_percentage, getRamTemperature()

def getRamTemperature():
    try:
        w = wmi.WMI(namespace=r"root\wmi")
        temperature_info = w.MSAcpi_ThermalZoneTemperature()

        for temp in temperature_info:
            # The temperature is given in tenths of Kelvin, converting it to Celsius
            temperature_celsius = (temp.CurrentTemperature / 10.0) - 273.15
            if "RAM" in temp.InstanceName.upper():
                #print(f"RAM Temperature: {temperature_celsius:.2f}°C")
                return temperature_celsius
        #print("RAM Temperature: Not available")
        return None
    except wmi.x_access_denied:
        #print("Access denied. Please run the script as an administrator.")
        return None

if __name__ == "__main__":
    total_memory, available_memory, used_memory, memory_percentage, temperature = ramUsage()
  
