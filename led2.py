from machine import Pin, Timer
from time import sleep
#led = Pin(25, Pin.OUT)
#timer = Timer()
leds = [ Pin(16, Pin.OUT),
         Pin(17, Pin.OUT),
         Pin(18, Pin.OUT),
         Pin(25, Pin.OUT)
       ]

#def blink(timer):
#    led.toggle()

def ledrun():
    for x in range(10):
        led.value(1)
        sleep(1)
        led.value(0)
        sleep(1)
        
def ledrun2():
    for i in leds:
        i.value(1)
        sleep(1)
        i.value(0)
        sleep(1)

ledrun2()

#timer.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)
#timer.init(freq=2.5, mode=Timer.PERIODIC, callback=ledrun)