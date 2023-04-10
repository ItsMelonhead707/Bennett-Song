#!/usr/bin/python3
from pijuice import PiJuice # Import pijuice module
from gpiozero import CPUTemperature
pijuice = PiJuice(1, 0x14) # Instantiate PiJuice interface object
print(pijuice.status.GetStatus()) # Read PiJuice status.

cpu = CPUTemperature()
print(cpu) # Read Raspberry Pi CPU Temperature