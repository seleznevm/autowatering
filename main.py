from machine import ADC
from machine import Pin
from time import sleep
# from umqttsimple import MQTTClient

pump = Pin(5, Pin.OUT)
global sensor
global water_level
water_level = Pin(16, Pin.IN)
adc = ADC(0)

def read():
    sensor = adc.read()
    print(sensor)
    
    sleep(1)

def pump_control():
    if sensor < 100: # and water_level.value() != 0:
        pump.on()
    else:
        pump.off()

#def MQTT_information:
#    if water_level.value() == 0:


while True:
    read()
    pump_control()

