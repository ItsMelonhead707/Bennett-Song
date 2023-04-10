#!/usr/bin/python3
from pijuice import PiJuice # Import pijuice module
import time
pijuice = PiJuice(1, 0x14) # Instantiate PiJuice interface object
print(pijuice.status.GetStatus()) # Read PiJuice status.

while True:
        pwr = pijuice.status.GetStatus() # Read PiJuice status
#       pijuice.status.SetLedState('D2', [0, 0, 0]) # Set PiJuice LED to Black
#       print('while1')
#       print(pijuice.status.GetStatus()) # Read PiJuice status
        while pwr['data']['powerInput'] == 'PRESENT':
                lvl = pijuice.status.GetChargeLevel()
                if lvl['data'] >= 90:
                        pijuice.status.SetLedState('D2', [0, 100, 0]) # Set PiJuice LE>
                pwr = pijuice.status.GetStatus() # Read PiJuice status
#       pijuice.status.SetLedState('D2', [0, 0, 0]) # Set PiJuice LED to Black
#               print(pijuice.status.GetStatus()) # Read PiJuice status
# print(lvl['data'])