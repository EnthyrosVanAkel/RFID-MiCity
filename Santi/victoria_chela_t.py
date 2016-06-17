import re, sys, signal, os, time, datetime
import serial
### Instalar Requets
import requests
import json


BITRATE = 9600


URL = 'http://10.1.8.170:9000/api/visitors/edad/'

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
      cadena = URL + match
      r = requests.put(cadena)
      json = r.json()
      print json
      edad = json.get('edad')
      chela = json.get('chelaFree')

      if edad:
        if !chela:
          print 'Permitido'
        else:
          print 'Entregada'
      else:
        print 'No Permitido'


