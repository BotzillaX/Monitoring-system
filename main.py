from getInfo import ramUsage #getting information about ram information
from time import sleep
import datetime 



def getCurrentDate():
    current_datetime = datetime.datetime.today()
    return current_datetime.strftime("%d-%m-%Y %H:%M:%S")
    

while True:
    sleep(0.1)
    currentDate = getCurrentDate() #Time
    totalMemory, available_memory, currently_using, currently_using_in_precentage, temperature = ramUsage() #RAM