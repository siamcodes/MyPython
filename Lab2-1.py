from machine import Pin
import time

p13 = Pin(13,Pin.OUT)

while True:
    p13.on()
    time.sleep_ms(1000)
    p13.off()
    time.sleep_ms(500)
