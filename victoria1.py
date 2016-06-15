import re, sys, signal, os, time, datetime
import serial
### Instalar Requets
import requests


BITRATE = 9600




if __name__ == '__main__':
    buffer = ''
    ser = serial.Serial('/dev/ttyUSB0', BITRATE, timeout=1)
    rfidPattern = re.compile(b'[\W_]+')
    while True:
      # Read data from RFID reader
      # 
      buffer = buffer + ser.read(ser.inWaiting())
      if '\n' in buffer:
        lines = buffer.split('\n')
        last_received = lines[-2]
        match = rfidPattern.sub('', last_received)
        print match
        buffer = ''
        lines = ''