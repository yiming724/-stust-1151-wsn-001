from machine import ADC
import time
 
sensor = ADC(ADC.CORE_TEMP)  # RP2350 內建溫度感測器
 
while True:
    raw = sensor.read_u16()  # 0 ~ 65535
    volt = raw * 3.3 / 65535
    temp = 27 - (volt - 0.706) / 0.001721
    print("temp = {:.1f} C".format(temp))
    time.sleep(2)

