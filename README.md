# Void Service Control (VSC)
## A simple script that will allow you to manage runit services in Void Linux

## Available on:
[![](https://cloud.orudo.ru/apps/files_sharing/publicpreview/RpcoJB8FwgNmqHC?file=/&fileId=48757&x=1920&y=1200&a=true&etag=10effec96382ba8b9fc181a5c1c85012)](https://git.orudo.ru/trueold89/void-service-control)
[![](https://cloud.orudo.ru/s/D8xtkTS8ZBCq8fC/download/GH.png)](https://github.com/Trueold89/void-service-control)

***

- [Installation](#install)
- [Usage](#usage)
- [Build from sources](#build-from_sources)
- [Example (Screenshot)](#example)


### Install:

**You can install vsc using pip:**

From [git.orudo.ru](https://git.orudo.ru/trueold89/void-service-control/releases):

```bash
$ pip install https://git.orudo.ru/trueold89/void-service-control/releases/download/0.2.1/VoidServiceControl-0.2.1.tar.gz
```
or pypi

```bash
$ pip install void-service-control
```

---

**Or by downloading the pre-built binary / xbps-package from the **[releases](https://git.orudo.ru/trueold89/void-service-control/releases)** page**

#### Install [.xbps package](https://git.orudo.ru/trueold89/void-service-control/releases):

```bash
& xbps-rindex -a *.xbps && xbps-install --repository=$PWD void-service-control
```

***

### Usage:

**Enbale service:**

```bash
$ vsc e <service_name>
```

**Disable service:**

```bash
$ vsc d <service_name>
```

**Action with multiple services:**
```bash
$ vsc e <first_service_name> <second_service_name>
```

**Print help:**

```bash
$ vsc --help
```
*All commands require root privileges*

### Build from sources

**Clone repo:**
```bash
$ git clone https://git.orudo.ru/trueold89/void-service-control.git --depth=1 && cd void-service-control
```

**Install deps:**
```bash
$ pip install setuptools
```

**Build sdist:**
```bash
$ python3 setup.py sdist
```

**Install:**
```bash
$ pip install dist/*
```

*Last command require root privileges*
***

## Example:


![](.ex.jpg)

