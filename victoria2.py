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
RECT_GREEN = [20, 20, 250, 100]

pygame.init()
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode(SCR_SIZE)




if __name__ == '__main__':
  buffer = ''
  ser = serial.Serial('/dev/ttyUSB0', BITRATE, timeout=1)
  rfidPattern = re.compile(b'[\W_]+')
  while True:
    buffer = buffer + ser.read(ser.inWaiting())
    if '\n' in buffer:
      lines = buffer.split('\n')
      last_received = lines[-2]
      match = rfidPattern.sub('', last_received)
      print match
      hexa = match[4:10]
      decimal = int(hexa,16)
      print decimal
      data = {'rfid':decimal,'zona':1,'experiencia':1}
      r = requests.get(URL,params = data)
      json = r.json()
      edad = json.get('edad')
      if (edad < '18'):
        pygame.draw.rect(screen,RED,RECT_RED)
        print 'No permitido'
      else:
        pygame.draw.rect(screen,GREEN,RECT_GREEN)
        print 'Permitido'
      
      buffer = ''
      lines = ''


    pygame.display.update()