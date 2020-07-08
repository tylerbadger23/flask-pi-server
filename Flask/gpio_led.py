from gpiozero import LEDBoard, LED
import time
led_state = [False, False, False, True] #R<G<B

RED_PIN = 13
GREEN_PIN = 19
BLUE_PIN = 26
run_count = 0

leds = LEDBoard(13, 19, 26, 4) #gpio pins

def display():
    leds.on()
    time.sleep(.3)
    leds.off(3)
    time.sleep(.3)
    leds.off(1)
    time.sleep(.3)
    leds.off(2)

def red ():
    leds.on(2)
    
def blue():
    leds.on(0)
    
def green ():
    leds.on(1)
def yellow():
    leds.on(3)
    time.sleep(.3)
    leds.off(0,1,2,3)
    
while run_count <= 2:
    for index, state in enumerate(led_state):
        if state == False:
            led_state[index] = True
            leds.on(index)
        else:
            led_state[index] = False
            leds.off(index)
            
    time.sleep(1)
    run_count += 1


time.sleep(1)
leds.off(1,2,3)