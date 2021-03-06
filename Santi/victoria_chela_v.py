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
BLUE = (0,0,255)
RECT = [0, 0, 320, 240]


pygame.init()
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode(SCR_SIZE)

#URL = 'http://10.0.1.100:8080/api/visitors/'
URL = 'http://10.1.8.170:9000/api/visitors/'

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
      pygame.draw.rect(screen,WHITE,RECT)
      line = ser.readline()
      last_received = line.strip()
      match = rfidPattern.sub('', last_received)
      print match
      cadena = URL + 'edad/' +match
      r = requests.get(cadena)
      json = r.json()
      print json
      edad = json.get('edad')
      chela = json.get('chelaFree')

      if edad == 'True':
        if not chela:
          print 'Permitido'
          pygame.draw.rect(screen,GREEN,RECT)
          c = requests.post(URL + 'free/' + match + '/true')
          #time.sleep(2)
          #pygame.draw.rect(screen,BLACK,RECT)
        else:
          print 'Entregada'
          pygame.draw.rect(screen,BLUE,RECT)
          #time.sleep(2)
          #pygame.draw.rect(screen,BLACK,RECT)
      else:
        print 'No Permitido'
        pygame.draw.rect(screen,RED,RECT)
        #time.sleep(2)
        #pygame.draw.rect(screen,BLACK,RECT)


      
      pygame.display.update()
      #time.sleep(2)
      #pygame.draw.rect(screen,BLACK,RECT)
