from getRam import ramUsage #getting information about ram information
from time import sleep, time 
from getCPU import cpuUsage
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
    print(currently_using_in_precentage)
    print(cpuUsage1)
    sleep(0.1)
    os.system('cls' if os.name == 'nt' else 'clear')
 