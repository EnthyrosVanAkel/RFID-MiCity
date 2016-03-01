import re, sys, signal, os, time, datetime
import serial
### Instalar Requets
import requests
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

URL = '127.0.0.1'
PORT = 5720
BITRATE = 9600


def encender():
    GPIO.output(11,True)
    time.sleep(1)
    GPIO.output(11,False)

def sumar_puntos(rfid,puntos):
    encender()
    url = 'http://papalote.cocoplan.mx/v0/agregar_puntos'
    data = {'rfid':rfid,'puntos':puntos}
    r = requests.post(url,data)
    print r


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
        sumar_puntos(str(decimal),'10')
        buffer = ''
        lines = ''
