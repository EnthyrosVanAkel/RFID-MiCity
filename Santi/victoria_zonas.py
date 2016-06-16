import re, sys, signal, os, time, datetime
import serial
### Instalar Requets
import requests
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(10,GPIO.OUT)

URL = 'http://10.1.8.170:9000/api/visitors/'
BITRATE = 9600
LED = False
ZONA = 'Comida'


def encender():
    GPIO.output(11,True)
    time.sleep(1)
    GPIO.output(11,False)

def mandar_zona(rfid,zona):
    if LED:
        encender()
    consulta = URL + rfid +'/' + zona
    print consulta
    r = requests.get(consulta)
    print r.toJson()


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
