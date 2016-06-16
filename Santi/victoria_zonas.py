import re, sys, signal, os, time, datetime
import serial
### Instalar Requets
import requests
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

URL = 'http://papalote.cocoplan.mx/v0/agregar_puntos'
BITRATE = 9600
LED = False
ZONA = 10

def encender():
    GPIO.output(11,True)
    time.sleep(1)
    GPIO.output(11,False)

def mandar_zona(rfid,zona):
    if LED:
        encender()
    data = {'rfid':rfid,'zona':1,'experiencia':1,'puntos':zona}
    r = requests.post(URL,data)
    print r


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
            rfid = line.strip()
            print rfid
            mandar_zona(rfid,ZONA)