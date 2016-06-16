import re, sys, signal, os, time, datetime
import serial
### Instalar Requets
import requests


BITRATE = 9600


URL = 'http://papalote.cocoplan.mx/v0/visitante'

if __name__ == '__main__':
    buffer = ''
    ser = serial.Serial('/dev/ttyUSB0', BITRATE)
    rfidPattern = re.compile(b'[\W_]+')
    while True:
      # Read data from RFID reader
      # 
	data = ser.read(12)
      #buffer = buffer + ser.read(ser.inWaiting())
      #if '\n' in buffer:
     #   lines = buffer.split('\n')
     #   last_received = lines[-2]
     #   match = rfidPattern.sub('', last_received)
	match = data
	ser.flushInput()	
        print match
        data = {'rfid':match,'zona':1,'experiencia':1}
        r = requests.get(URL,params = data)
        json = r.json()
        edad = json.get('edad')
        if (edad < '18'):
          #pygame.draw.rect(screen,RED,RECT_RED)
          print 'No permitido'
        else:
          #pygame.draw.rect(screen,GREEN,RECT_GREEN)
          print 'Permitido'
      
        buffer = ''
        lines = ''
