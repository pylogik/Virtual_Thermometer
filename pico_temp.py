from machine import ADC, UART
from time import sleep

temp_sensor = ADC(4)
temperature = temp_sensor.read_u16()

to_volts = 3.3 / 65535
temperature = temperature * to_volts

celsius_degrees = 27 - (temperature - 0.706) / 0.001721

fahrenheit_degrees = celsius_degrees * 9 / 5 + 32

uart =  machine.UART(1, baudrate=9600)

def thermo():
    print(f'Celsius; {celsius_degrees}, Fahrenheit; {fahrenheit_degrees}')
    uart.read()
    sleep(1)

while True:
    thermo()


