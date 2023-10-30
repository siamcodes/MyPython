from machine import Pin, PWM
import time
import math

led = PWM(Pin(16), freq= 1000, duty=0)

def pulse(l, t):
    for i in range(20):
        l.duty(int(math.sin(i/10*math.pi)*500+500))
        time.sleep_ms(t);
    

while True:
    pulse(led,50)
    time.sleep(1)  #1s
    for i in range(10):  #loop 0-9
        pulse(led,20)