#!/usr/bin/python3
from pijuice import PiJuice # Import pijuice module
from gpiozero import CPUTemperature
import time
import json

pijuice = PiJuice(1, 0x14) # Instantiate PiJuice interface object
# print(pijuice.status.GetStatus()) # Read PiJuice status.
# print('Battery Level', pijuice.status.GetChargeLevel()) # Read Battery Level and Cha>
# temp = pijuice.status.GetBatteryTemperature()
# print(temp) # Read Battery Temperature

cpu = CPUTemperature()
# print(cpu.temperature)  # Read CPU Temperature
# print(pijuice.status.SetLedState('D2', [0, 0, 0])) # Set PiJuice LED state to black

while True:
        if cpu.temperature >= 75:
                print(pijuice.status.SetLedState('D2', [255, 0, 0])) # Set PiJuice LED>
        if cpu.temperature >= 60 and cpu.temperature < 75:
                print(pijuice.status.SetLedState('D2', [155, 0, 155])) # Set PiJuice L>
        if cpu.temperature >= 50 and cpu.temperature < 60:
                print(pijuice.status.SetLedState('D2', [175, 255, 0])) # Set PiJuice L>
        if cpu.temperature < 50:
                print(pijuice.status.SetLedState('D2', [0, 0, 255])) # Set PiJuice LED>
        time.sleep(10)