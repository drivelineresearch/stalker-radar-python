# Serial Port Data Logger

## Introduction
This project provides a Python script for reading data from a serial port and logging it to a file. It's particularly useful for applications involving data acquisition from serial devices like sensors, modems, etc.

## Features
- Reads data from a specified serial port.
- Logs data with timestamp to a file.
- Handles errors and continues operation.

## Requirements
- Python 3.x
- PySerial package
- Any device that transmits data via a serial port.

## Installation
1. Clone this repository or download the source code.
2. Install Python 3.x if not already installed.
3. Install PySerial using pip:
   
`pip install pyserial`
   
## Usage
1. Modify the SERIAL_PORT in the script to match the port your device is connected to.
2. Optionally, change the LOG_FILE path to your desired log file location.
3. Run the script:

`python serial_logger.py`
