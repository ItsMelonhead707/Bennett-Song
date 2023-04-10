#!/usr/bin/python3
from pijuice import PiJuice # Import pijuice module
import time
pijuice = PiJuice(1, 0x14) # Instantiate PiJuice interface object
print(pijuice.status.GetStatus()) # Read PiJuice status.

while True:
        pwr = pijuice.status.GetStatus() # Read PiJuice status
        while pwr['data']['powerInput'] == 'NOT_PRESENT':
                lvl = pijuice.status.GetChargeLevel()
                pwr = pijuice.status.GetStatus()
                if lvl['data'] <= 15:
                        pijuice.status.SetLedBlink('D2', 1, [160, 0, 100], 1000, [100,>
                        time.sleep(2)
