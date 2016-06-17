import re, sys, signal, os, time, datetime
import serial
### Instalar Requets
import requests


BITRATE = 9600


URL = ' http://10.1.8.170:9000/api/visitors/edad/'

if __name__ == '__main__':
  ser = serial.Serial('/dev/ttyUSB0', BITRATE)
  rfidPattern = re.compile(b'[\W_]+')
  try:
    ser.flushInput()
    ser.flushOutput()
  except Exception, e:
    print "error open serial port: " + str(e)
    exit()

  if ser.isOpen():
    while True:
      line = ser.readline()
      last_received = line.strip()
      match = rfidPattern.sub('', last_received)
      print match
      #data = {'rfid':match,'zona':1,'experiencia':1}
      #r = requests.get(URL,params = data)
      #json = r.json()
