import re, sys, signal, os, time, datetime
import serial
### Instalar Requets
import requests
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

URL = '10.1.8.170:9000/api/visitors/'
BITRATE = 9600
<<<<<<< HEAD
LED = True
ZONA = 10
=======
LED = False
ZONA = 'Comida'
>>>>>>> 5c52870b5027c333c2d58485b3d73a4090832bc1

def encender():
    GPIO.output(11,True)
    time.sleep(1)
    GPIO.output(11,False)

def mandar_zona(rfid,zona):
    if LED:
        encender()
    consulta = URL + rfid +'/' zona
    r = requests.get(consulta)
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
