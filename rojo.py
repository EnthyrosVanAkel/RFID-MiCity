import re, sys, signal, os, time, datetime
import serial
### Instalar Requets
import requests
import json
import pygame


os.environ["SDL_FBDEV"] = "/dev/fb1"
os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
os.environ["SDL_MOUSEDRV"] = "TSLIB"
BITRATE = 9600
URL = 'http://papalote.cocoplan.mx/v0/visitante'



if __name__ == '__main__':
    buffer = ''
    ser = serial.Serial('/dev/ttyUSB0', BITRATE, timeout=1)
    rfidPattern = re.compile(b'[\W_]+')
    visitante = 12
    eleccion = 10
    while True:
      # Read data from RFID reader
      buffer = buffer + ser.read(ser.inWaiting())
      if '\n' in buffer:
        lines = buffer.split('\n')
        last_received = lines[-2]
        match = rfidPattern.sub('', last_received)
        hexa = match[4:10]
        decimal = int(hexa,16)
        print decimal
        data = {'rfid':decimal,'zona':1,'experiencia':1}
        r = requests.get(URL,params = data)
        json = r.json()
	print json.get('edad') 
        buffer = ''
        lines = ''
