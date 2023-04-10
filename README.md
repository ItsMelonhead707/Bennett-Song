<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<h3 align="center">Bennett-Song</h3>

  <p align="center">
    A self-contained song library on your phone browser through a static site. 
    <br />
    <a href="https://github.com/ItsMelonhead707/Bennett-Song"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/ItsMelonhead707/Bennett-Song">View Demo</a>
    ·
    <a href="https://github.com/ItsMelonhead707/Bennett-Song/issues">Report Bug</a>
    ·
    <a href="https://github.com/ItsMelonhead707/Bennett-Song/issues">Request Feature</a>
  </p>
</div>




<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Bennett-Song-Screenshot][product-screenshot-outcase]](https://github.com/ItsMelonhead707/Bennett-Song/images/screenshot.png)
<br />
A raspberry pi powered device for remote viewing of your song library.
It uses [jmb05/onsong-parser-go](https://github.com/jmb05/onsong-parser-go) 
to create a static site for the song-library.
It was made because we wanted to share our songs with people for a gathering without
everyone owning the Onsong App and not being able to project the lyrics onto a screen for everyone.
This Project was intended to work at places without internet or a pre existing network! (e.g. the beach)

You connect your smartphone to the Bennett-Song Network 
and have a song library to play guitar and sing from.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow the steps below.

### What you'll need
* [Raspberry Pi Zero 2 w](https://www.reichelt.com/raspberry-pi-zero-2-w-4x-1-ghz-512-mb-ram-wlan-bt-rasp-pi-zero2-w-p313902.html) (or any other one)
* [micro SD Card](https://www.reichelt.de/microsdhc-speicherkarte-16gb-intenso-uhs-i-professional-intenso-3433470-p158171.html)
* [PiJuice Zero](https://uk.pi-supply.com/products/pijuice-zero) (or the [Standard](https://uk.pi-supply.com/collections/pijuice/products/pijuice-standard))
* [Battery](https://uk.pi-supply.com/products/pijuice-zero-1000mah-battery) (at least 1000 mAh)
* [heat sink](https://www.waveshare.com/zero-heatsink.htm)
* [Wifi dongle](https://www.reichelt.de/wlan-adapter-usb-150-mbit-s-tplink-tl-wn725n-p123963.html) 
* [micro USB adapter](https://www.amazon.de/-/en/KiwiBird-Connector-Compatible-Smartphones-Function-Silver/dp/B01FPZGCUQ/ref=sr_1_4?crid=2GHHTOIM4GQD5&keywords=micro+usb+auf+usb+b+adapter&qid=1679823702&sprefix=micro+usb+to+usb+b+adapt%2Caps%2C166&sr=8-4) (only for Raspberry Pi Zero)
* [GPIO header](https://www.reichelt.de/raspberry-pi-gpio-header-40-polig-rm-2-54-farblich-kodiert-rpi-header-cg4-p291479.html?&trstct=pos_0&nbc=1) & [GPIO header for soldering](https://www.reichelt.de/raspberry-pi-gpio-header-40-polig-rm-2-54-farblich-kodiert-rpi-header-cg1-p239855.html) (optional)
* some kind of case

### Prerequisites

You'll need a fresh install of raspbian on your micro SD card
([RaspberryPi Website](https://www.raspberrypi.com/software/)).

### Put the hardware together
Take the Raspberry Pi and stick the heat sink to it.
Then connect the Raspberry Piand the PiJuice via the GPIO Pins and connect the battery to the PiJuice hat
(You might need to solder a GPIO header to the Raspberry Pi if there aren't any yet).
Connect the Wifi dongle and place it in the case.


### Installation

1. Install the PiJuice software
   ```sh
   sudo apt install pijuice-base
   ```
   or 
   <br />
   ```sh
   sudo apt install pijuice-gui
   ```
   if you want a gui (but we will be using the base version)
   <br />
2. Open the PiJuice Software and configure the PiJuice hat
   ```sh
   pijuice_cli
   ```
   * Navigate to the **"Status"** section and check if the battery is connected properly and charging.
   * Navigate to the **"Buttons"** section and **"SW1"** and change **"LONG_PRESS1"** to **"USER_FUNC1"** : **"5000"**.
   * Navigate to **"LEDs"**, leave the **"D1"** LED as is at **"CHARGE STATUS"** but change the **"D2"** LED to **"USER LED"** we are going to use it with a python programm later. Dont forget to **""Apply Settings"**.
   * Navigate to **"Battery Profile"** and under **"Profile"** change it to the correct battery type (depending on your battery). If you have one from PiSupply otherwise change to custom and instert the values. Dont forget to **"Apply Settings"**. (if you have set this using the DIP switches on the PiJuice you can skip this step)
   * Navigate to **"Firmware"** and check if the Firmware is up to date and if not update it.
   * Navigate to **"System Task"** and enable **"System Task"** as well as **"Min charge"** and set that value to 10%. Dont forget to **"Apply Settings"**.
   * Navigate to **"System Events"**  and set **"Low charge"** to **"USER_FUNC1"**. Dont forget to **"Apply Settings"**.
   * Navigate to **"User Scripts"** and set **"USER_FUNC_1"** to `pi/home/shutdown.py` (or the place and name you want of your shutdown script; we will make it shortly)
   or
   ```sh
   cd 
   curl https://raw.githubusercontent.com/PiSupply/PiJuice/master/Software/Source/Utilities/pijuice_util.py > pijuice_util.py  
   ```
   ```sh
   
   ```
   
   
3. Setting the System Clock & RTC (RealTimeClock)

   ##### check the PiJuice RTC is connected via ID EEPROM

   ```sh
   i2cdetect -y 1
   ```
   where you will see **"UU"** at adress 68
   ```sh
   pi@rpi-stretch-full:~ $ i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
   00:          -- -- -- -- -- -- -- -- -- -- -- -- --
   10: -- -- -- -- 14 -- -- -- -- -- -- -- -- -- -- --
   20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
   30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
   40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
   50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
   60: -- -- -- -- -- -- -- -- UU -- -- -- -- -- -- --
   70: -- -- -- -- -- -- -- --                         
   pi@rpi-stretch-full:~ $
   ```
   If your ID EEPROM address is set to 0x52 (Which you will need to change if stacking another HAT) then you will need to manually load the driver in the `/boot/config.txt` by adding the following line:
   
   ```sh 
   # RTC PiJuice
   dtoverlay=i2c-rtc,ds1339
   ```
   you need to reboot your Raspberry Pi after changing the config file
   ```sh
   sudo reboot
   ```
   
   ##### setting the system Clock & RTC
   
   There are two ways in which you can set your system time and date providing that you have set the timezone in Raspbian; automatically using timesync or manually in the command line. If you have an internet connection then the time will automatically be synched after boot and this will also sync with the RTC time.
   <br />
   Manually you can set the time with the `date` command from the command line`
   
   ```sh
   sudo date -s '2018-10-29 12:30:46' 
   ```
   
   After setting the date and time you must then copy the system time to the RTC with the command:
   
   ```sh
   sudo hwclock -w
   ```
   
   You can check this with:
   
   ```sh
   sudo hwclock -r   
   ```
   
   ##### Sync RTC time at boot
   
   When the Raspberry Pi shutsdown and then reboots you must copy the RTC time
   back to the system clock at boot and you can 
   do this in `/etc/rc.local` with `sudo hwclock -s`.
   <br />
   <br />
   Note: This assumes that your PiJuice has sufficient power from the battery to keep the simulated RTC running in the PiJuice microcontroller while the Pi is shut down.
4. create the shutdown script `shutdown.py`
   ```
   cd
   sudo nano shutdown.py
   ```
   now write:
   ```py
   #!/usr/bin/python3

   from pijuice import PiJuice
   import os
   pijuice = PiJuice(1, 0x14)

   #Remove power to PiJuice MCU IO pins
   pijuice.power.SetSystemPowerSwitch(0)

   #Set wakeup
   pijuice.power.SetWakeUpOnCharge('DISABLED')

   #Remove 5V power to RPI after 60 seconds
   pijuice.power.SetPowerOff(60)

   #Shut down the RPI
   os.system("sudo halt")


   ```
5. create a LED folder
   ```sh
   cd
   mkdir "LED"
   ```
6. create the cpu temperature LED script `cpu-temperature.py`
   ```sh
   cd LED
   sudo nano cpu-temperature.py
   ```
   now write
   ```py
   #!/usr/bin/python3
   from pijuice import PiJuice # Import pijuice module
   from gpiozero import CPUTemperature
   pijuice = PiJuice(1, 0x14) # Instantiate PiJuice interface object
   print(pijuice.status.GetStatus()) # Read PiJuice status.

   cpu = CPUTemperature()
   print(cpu) # Read Raspberry Pi CPU Temperature
   ```
   
9. create LED scripts

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
[![Bennett-Song-Zero-Case][product-screenshot-incase-option-one]](https://github.com/ItsMelonhead707/images/bennett-song-zero-case.png)
[![Bennett-Song-Four-Case][product-screenshot-incase-option-two]](https://github.com/ItsMelonhead707/images/bennett-song-four-case.png)
<br />
<br />
You power it on via the PiJuice button and wait for completed booting.
Connect with your phone to the Wifi network called SongNet (or whatever you named it) via a QR-Code or just through the Settings App.
Then use the website QR-Code to load the static site or use the ip adress (e.g.: [3.14.15.9](https://3.14.15.9) *like our one* :joy:).
<br />
<br />
[![Bennett-Song-Screenshot-1][product-screenshot-1]](https://github.com/ItsMelonhead707/images/screenshot-1.png)
[![Bennett-Song-Screenshot-2][product-screenshot-2]](https://github.com/ItsMelonhead707/images/screenshot-2.png)
<br />
<br />
Navigate to the song you want and use the link to get to it. 
If you need to get back to the homepage use the home button or just use the last page button existing in every browser.
To turn it off just press the PiJuice button for 10 seconds and it will shutdown safely.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

ItsMelonhead707 - jib_03a@web.de

Project Link: [https://github.com/ItsMelonhead707/Bennett-Song](https://github.com/ItsMelonhead707/Bennett-Song)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [README Template](https://github.com/othneildrew/Best-README-Template)
* [Onsong Parser (GO)](https://github.com/jmb05/onsong-parser-go)
* [Onsong Parser (Haskell - not used)](https://github.com/josiah-bennett/Onsong-Parser)
* [Onsong SSG (not used)](https://github.com/josiah-bennett/Onsong-SSG)
* [PiJuice](https://github.com/PiSupply/PiJuice/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/ItsMelonhead707/Bennett-Song.svg?style=for-the-badge
[contributors-url]: https://github.com/ItsMelonhead707/Bennett-Song/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ItsMelonhead707/Bennett-Song.svg?style=for-the-badge
[forks-url]: https://github.com/ItsMelonhead707/Bennett-Song/graphs/forks
[stars-shield]: https://img.shields.io/github/stars/ItsMelonhead707/Bennett-Song.svg?style=for-the-badge
[stars-url]: https://github.com/ItsMelonhead707/Bennett-Song/graphs/stars
[issues-shield]: https://img.shields.io/github/issues/ItsMelonhead707/Bennett-Song.svg?style=for-the-badge
[issues-url]: https://github.com/ItsMelonhead707/Bennett-Song/issues
[license-shield]: https://img.shields.io/github/license/ItsMelonhead707/Bennett-Song.svg?style=for-the-badge
[license-url]: https://github.com/ItsMelnhead707/Bennett-Song/blob/master/LICENSE.txt
[product-screenshot-outcase]: images/bennett-song.png
[product-screenshot-incase-option-one]: images/bennett-song-zero-case.png
[product-screenshot-incase-option-two]: images/bennett-song-four-case.png
[product-screenshot-1]: images/screenshot-1.png
[product-screenshot-2]: images/screenshot-2.png