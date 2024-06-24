from getRam import ramUsage #getting information about ram information
from time import sleep, time 
from getCPU import cpuUsage
from getGPU import print_gpu_load
import datetime 
import os


def getCurrentDate():
    current_datetime = datetime.datetime.today()
    return current_datetime.strftime("%d-%m-%Y %H:%M:%S")
    

while True:

    
    currentDate = getCurrentDate() #Time
    totalMemory, available_memory, currently_using, currently_using_in_precentage, temperature = ramUsage() #RAM
    cpuUsage1 = cpuUsage()
    print(currentDate)
    print("Memory-Usage: " + str(currently_using_in_precentage) + "%")
    print("CPU-Usage: " + str(cpuUsage1) + "%")
    print("GPU-Usage: " + str(print_gpu_load())+ "%")
    sleep(0.1)
    os.system('cls' if os.name == 'nt' else 'clear')
 