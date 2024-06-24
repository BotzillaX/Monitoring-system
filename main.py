from getInfo import ramUsage
from time import sleep
import datetime 


while True:
    current_datetime = datetime.datetime.today()
    time_and_date_str = current_datetime.strftime("%d-%m-%Y %H:%M:%S")
    print(time_and_date_str)
    sleep(0.1)
    ramUsage()