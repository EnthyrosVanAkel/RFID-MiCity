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

SCR_SIZE = 320, 240
WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
YELLOW = (0,0,255)
RECT_RED = [20, 0, 250, 80]
RECT_GREEN = [20, 80, 250, 80]
RECT_YELLOW = [20, 160, 250, 80]


pygame.init()
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode(SCR_SIZE)

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
          pygame.draw.rect(screen,GREEN,RECT_GREEN)
        else:
          print 'Entregada'
          pygame.draw.rect(screen,YELLOW,RECT_YELLOW)
      else:
        print 'No Permitido'
        pygame.draw.rect(screen,RED,RECT_RED)


      pygame.display.update()




