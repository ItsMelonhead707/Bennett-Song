#!/usr/bin/python3
from pijuice import PiJuice # Import pijuice module
import time
pijuice = PiJuice(1, 0x14) # Instantiate PiJuice interface object
print(pijuice.status.GetStatus()) # Read PiJuice status.
print(pijuice.status.GetBatteryTemperature())
# print(pijuice.status.GetLedState('D1'))
# print(pijuice.status.GetLedState('D2'))
print(pijuice.status.SetLedState('D2', [0, 0, 0]))
pijuice.status.SetLedBlink('D2', 2, [0,200,100], 1000, [100, 0, 0], 1000)
time.sleep(4)
pijuice.status.SetLedBlink('D2', 1,[175, 222, 52], 1000, [0, 0, 52], 1000)
time.sleep(2)
pijuice.status.SetLedBlink('D2', 1,[144, 155, 52], 1000, [55, 0, 134], 1000)
time.sleep(2)
pijuice.status.SetLedBlink('D2', 1,[144, 155, 52], 1000, [1, 0, 134], 1000)
time.sleep(2)
pijuice.status.SetLedBlink('D2', 1,[144, 155, 52], 1000, [55, 79, 134], 1000)
time.sleep(2)
pijuice.status.SetLedBlink('D2', 1,[144, 155, 52], 1000, [73, 0, 57], 1000)
time.sleep(2)

print(pijuice.status.SetLedState('D2', [144, 155, 52]))