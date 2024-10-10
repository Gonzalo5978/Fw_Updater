<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br/>
<div align="center">
  <a href="https://github.com/Gonzalo5978/Fw_Updater">
    <img src="logo.webp" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Firmware Updater</h3>

  <p align="center">
    Command Line tool for update device Firmwares via API
    <br />
    <a href="https://github.com/Gonzalo5978/Fw_Updater"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/Gonzalo5978/Fw_Updater">View Demo</a>
    ·
    <a href="https://github.com/Gonzalo5978/Fw_Updater/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/Gonzalo5978/Fw_Updater/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
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
    <ul>
    <li><a href="#python-3.12">Python 3.12</a></li>
            <ul>
                <li><a href="#debian">Debian</a></li>
                <li><a href="#fedora">Fedora</a></li>
            </ul>
    </ul>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

<p>Project made by Gonzalo Rodríguez.</p>
<p>This project aims to automate firmware update process by API on compatible devices. This utility removes the </p>
<p>The received element should contain data of a CCTV model such as security cameras. Actually the API is able to comunicate with Hikvisio ISAPI based devices in order to check it's configurations and change parameters remotely.</p>

<p>Actual API's implemented:</p>
<ul>
  * Hikvision (ISAPI)
</ul>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* [![Python][Python]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
# Getting Started

## Prerequisites

<p>Follow the steps to install project dependencies.</p>

<!-- PYTHON-3.12 INSTALL -->
### Python-3.13 Installation
<!-- Debian -->
* <b>Debian</b>

1. Update system:

    ```sh
    sudo apt update -y
    sudo apt upgrade -y
    ```

2. Install dependencies:

    ```sh
    sudo apt install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
    libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
    xz-utils tk-dev libffi-dev liblzma-dev python3-openssl git
    ```

3. Download source code:

    ```sh
    wget https://www.python.org/ftp/python/3.13.0/Python-3.13.0.tgz
    ```

4. Extract files:

    ```sh
    tar -xf Python-3.13.0.tgz
    ```

5. Configure and build:

    ```sh
    cd Python-3.13.0
    ./configure --enable-optimizations
    ```

6. Build Python:

    ```sh
    make -j 4
    ```

7. Install:

    ```sh
    sudo make altinstall
    ```

    <small><i>Using altinstall instead of install prevents it from replacing the system's default Python interpreter (which could cause system tools to malfunction).</i></small>

8. Verify Installation:

    ```sh
    python3.13 --version
    ```

<!-- Fedora -->
* <b>Fedora</b>

1. Update system:

    ```sh
    sudo dnf update
    ```

2. Install dependencies:

    ```sh
    sudo dnf groupinstall 'Development Tools'
    sudo dnf install openssl-devel bzip2-devel libffi-devel sqlite-devel 
    ```

3. Download source code:

    ```sh
    wget https://www.python.org/ftp/python/3.13.0/Python-3.13.0.tgz
    ```

4. Extract files:

    ```sh
    tar -xf Python-3.13.0.tgz
    ```

5. Configure and build:

    ```sh
    cd Python-3.13.0
    ./configure --enable-optimizations
    ```

6. Build Python:

    ```sh
    make -j 4
    ```

7. Install:

    ```sh
    sudo make altinstall
    ```

    <small><i>Using altinstall instead of install prevents it from replacing the system's default Python interpreter (which could cause system tools to malfunction).</i></small>

8. Verify Installation:

    ```sh
    python3.12 --version
    ```

## Installation

<p>To use the tool correctly follow this steps:</p>

1. Clone repository

    ```sh
    git clone https://github.com/Gonzalo5978/Fw_Updater.git
    ```

2. Open directory

    ```sh
    cd Fw_Updater
    ```

3. Activate virtual enviroment

    ```sh
    source venv/bin/activate
    ```

4. Install dependencies

    ```sh
    pip install -r requirements.txt
    ```

<!-- USAGE EXAMPLES -->
## Usage

```sh
python run.py --ip <device_ip> --password <device_password> --port <http_port (optional)>
```

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

* [x] Update Hikvision devices

See the [open issues](https://github.com/Gonzalo5978/Fw_Updater/issues) for a full list of proposed features (and known issues).

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

<br>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Top contributors

<a href="https://github.com/Gonzalo5978/Fw_Updater/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Gonzalo5978/Fw_Updater" alt="contrib.rocks image" />
</a>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Gonzalo Rodríguez - <gon.cyber@protonmail.com>

Project Link: [https://github.com/Gonzalo5978/Fw_Updater](https://github.com/Gonzalo5978e/Fw_Updater)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/Gonzalo5978/Fw_Updater.svg?style=for-the-badge
[contributors-url]: https://github.com/Gonzalo5978/Fw_Updater/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Gonzalo5978/Fw_Updater.svg?style=for-the-badge
[forks-url]: https://github.com/Gonzalo5978/Fw_Updater/network/members
[stars-shield]: https://img.shields.io/github/stars/Gonzalo5978/Fw_Updater.svg?style=for-the-badge
[stars-url]: https://github.com/Gonzalo5978/Fw_Updater/stargazers
[issues-shield]: https://img.shields.io/github/issues/Gonzalo5978/Fw_Updater.svg?style=for-the-badge
[issues-url]: https://github.com/Gonzalo5978/Fw_Updater/issues
[license-shield]: https://img.shields.io/github/license/Gonzalo5978/Fw_Updater.svg?style=for-the-badge
[license-url]: https://github.com/Gonzalo5978/Fw_Updater/blob/master/LICENSE.txt
[product-screenshot]: images/screenshot.png
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/
