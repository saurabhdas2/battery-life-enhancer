# -*- coding: utf-8 -*-
"""

@author: Saurabh Das
"""
import psutil
import time
from plyer import notification


# function returning time in hh:mm:ss
def convertTime(seconds):
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    return "%d:%02d:%02d" % (hours, minutes, seconds)


while(True):
    
# returns a tuple
    battery = psutil.sensors_battery()
    
    print("Battery percentage : ", battery.percent)
    print("Power plugged in : ", battery.power_plugged)
    
    # converting seconds to hh:mm:ss
    print("Battery left : ", convertTime(battery.secsleft))
    
    if(battery.power_plugged == True and battery.percent >= 70):
        print("unplug charger")
        msg = "Unplug charger"
        notification.notify(
        title="Battery Life Enhancer",
        message=msg,
        timeout=5
        )        
    elif(battery.power_plugged == False and battery.percent <= 30):
        print("plug in charger")
        msg = "plug in the charger"
        notification.notify(
        title="Battery Life Enhancer",
        message=msg,
        timeout=5
        )
    

    time.sleep(60*20)
        
#    continue
