from machine import Pin, PWM, ADC
import time

r = PWM(Pin(18))
r.freq(1000)
g = PWM(Pin(19))
g.freq(1000)
b = PWM(Pin(20))
b.freq(1000)

pot = ADC(Pin(26))
#pot.atten(ADC.ATTEN_11DB) # maximum 3.6V
#pot.width(ADC.WIDTH_12BIT) # 12bit 0 to 4095

def map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

medium = 2030  #ADC: 0(min) - 4095(max)
gap = 200      # +/- Gap
duty = 0       #duty cycle

while True:
    adc = pot.read_u16()
    print('ADC:', adc, end='>>')
    
    if adc > (medium+gap):
        duty = map(adc,)
    