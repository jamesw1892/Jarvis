# Introduction

Jarvis is an open source virtual assistant designed to work on any device.

# Usage

Run `Jarvis.py` to auto-detect the system you are on and run the relevant file. Otherwise, you can run the file yourself; currently supported systems are:

- Windows (`OSWindows.py`)
- Android (`OSAndroid.py`)
- Raspian Linux (`OSRaspian`)

# Improvements

There are 2 main ways to improve Jarvis:

## Adding support for new systems

If you want to run Jarvis on a system not yet supported, you can add support for it yourself. Use the guidance in `DESIGN.md`, the template `OSTemplate.py` and the existing supported systems as examples, e.g.: `OSWindows.py`. Then please submit a pull request so we can publish your work for everyone to enjoy!

## The core

Currently, Jarvis is hard-coded but I intend to add machine learning so Jarvis can learn how to respond.