import re, sys, signal, os, time, datetime
import serial
### Instalar Requets
import requests
import json
import pygame

BITRATE = 9600
URL = 'http://papalote.cocoplan.mx/v0/visitante'
SCR_SIZE = 320, 240
WHITE = (255, 255, 255)



if __name__ == '__main__':
    buffer = ''
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
    


