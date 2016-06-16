import re, sys, signal, os, time, datetime
import serial
### Instalar Requets
import requests
import pygame


os.environ["SDL_FBDEV"] = "/dev/fb1"
os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
os.environ["SDL_MOUSEDRV"] = "TSLIB"

BITRATE = 9600
URL = 'http://papalote.cocoplan.mx/v0/visitante'
SCR_SIZE = 320, 240
WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
RECT_RED = [20, 20, 250, 100]
RECT_GREEN = [20, 140, 200, 100]

pygame.init()
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode(SCR_SIZE)




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
        data = {'rfid':rfid,'zona':1,'experiencia':1}
        r = requests.get(URL,params = data)
        json = r.json()
        edad = json.get('edad')
        if (edad < '18'):
          pygame.draw.rect(screen,GREEN,RECT_GREE)
          print 'No permitido'
        else:
          pygame.draw.rect(screen,GREEN,RECT_GREEN)
          print 'Permitido'


        screen.fill(BLACK)

        pygame.display.update()
