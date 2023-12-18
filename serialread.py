import time
import serial
import logging
from datetime import datetime

# Constants
SERIAL_PORT = '/dev/ttyUSB0' # typical FTDI interface name
LOG_FILE = '/path/to/logfile.log'  # Replace with your desired log file path

# Set up logging
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s %(message)s')

# Function to read data from serial port
def read_serial_data(ser):
    if not ser.isOpen():
        ser.open()
    ser_bytes = ser.readline()
    return ser_bytes.decode('utf-8', 'ignore').strip()

# Main loop
def main():
    ser = serial.Serial(SERIAL_PORT)
    while True:
        try:
            data = read_serial_data(ser)
            if data:
                logging.info(f"Data: {data}")
                print(f"Data: {data}")
        except Exception as e:
            logging.error(f"Error: {e}")
            time.sleep(1)  # Delay to prevent rapid error logging in case of continuous failure

if __name__ == "__main__":
    main()
