from picamera import PiCamera 
import time
import os
import datetime
import globals
import gpio_led

def take_still (save_location):
    gpio_led.yellow()
    cam = PiCamera()
    cam.vflip = True
    timestamp = datetime.datetime.now()
    file_name = str(timestamp) + ".jpg"
    file_path = save_location + "/" + file_name
    cam.capture(file_path)
    cam.close()
    return file_name
