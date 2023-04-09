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
* Raspberry Pi 
* micro SD Card 
* PiJuice (Standard or Zero)
* Battery (at least 1000 mAh)
* heat sink
* Wifi dongle (& micro USB adapter if you are using a Raspberry Pi Zero)
* GPIO adapter & GPIO header (optional)
* some kind of case

### Prerequisites

You'll need a fresh install of raspbian on your micro SD card.
[RaspberryPi Website](https://www.raspberrypi.com/Software)

#### Put the hardware it together
Take the Raspberry Pi and stick the heat sink to it.
Then connect the Raspberry Piand the PiJuice via the GPIO Pins and connect the battery to the PiJuice hat
(You might need to solder a GPIO header to the Raspberry Pi if there aren't any yet).
Connect the Wifi dongle and place it in the case.


### Installation

1. Put a fresh install of raspbian on the micro SD card.
2. Clone the repo
   ```sh
   git clone https://github.com/ItsMelonhead707/Bennett-Song.git
   ```
3. Install NPM packages
   ```sh
   npm install
   ```
4. Enter your API in `config.js`
   ```js
   const API_KEY = 'ENTER YOUR API';
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage
[![Bennett-Song-Zero-Case][product-screenshot-incase-option-one]](https://github.com/ItsMelonhead707/images/bennett-song-zero-case.png)
[![Bennett-Song-Four-Case][product-screenshot-incase-option-two]](https://github.com/ItsMelonhead707/images/bennett-song-four-case.png)
<br />
<br />
You power it on via the PiJuice button and wait for completed booting.
Connect with your phone to the Wifi network called SongNet (or whatever you named it) via a QR-Code or just through the Settings App.
Then use the website QR-Code to load the static site or use the ip adress (e.g.: 3.14.15.9).
<br />
<br />
[![Bennett-Song-Screenshot-1][product-screenshot-1]](https://github.com/ItsMelonhead707/images/screenshot-1.png)
[![Bennett-Song-Screenshot-2][product-screenshot-2]](https://github.com/ItsMelonhead707/images/screenshot-2.png)
<br />
<br />
Navigate to the song you want and use the link to get to it. 
If you need to get back to the homepage use the home button or just use the last page button existing in every browser.
To turn it off ...


<br />
It was intended to work at places without internet or a network! (e.g. the beach)
You connect your smartphone to the Bennett-Song Network 
and have a song library to play guitar and sing from.
This is the [website](https://3.14.15.9) if your in the Bennett-Song network
<br />
Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

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