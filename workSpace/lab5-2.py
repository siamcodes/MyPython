from machine import Pin,ADC
import time
adc = ADC(Pin(2))
adc.atten(ADC.ATTN_0DB)
adc.width(ADC.WIDTH_12BIT)
vr = 0

while True:
  vr=adc.read() * 0.000805
  print(vr)
  time.sleep(1)
