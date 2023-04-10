#!/usr/bin/python3

from pijuice import PiJuice
import os
pijuice = PiJuice(1, 0x14)

#Remove power to PiJuice MCU IO pins
pijuice.power.SetSystemPowerSwitch(0)

#Set wakeup
pijuice.power.SetWakeUpOnCharge('DISABLED')

#Remove 5V power to Raspberry Pi after 60 seconds
pijuice.power.SetPowerOff(60)

#Shut down the Raspberry Pi
os.system("sudo halt")