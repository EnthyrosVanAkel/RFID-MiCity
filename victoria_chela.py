import re, sys, signal, os, time, datetime
import serial
### Instalar Requets
import requests
import pygame
import json

os.environ["SDL_FBDEV"] = "/dev/fb1"
os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
os.environ["SDL_MOUSEDRV"] = "TSLIB"

SCR_SIZE = 320, 240
BUTTON_PADDING = 10
WHITE = (255, 255, 255)

BITRATE = 9600


DEFAULT_CONFIG = {
    "address": "http://10.1.8.170:9000/api/visitors/"
  }


MENOR = {
    "label": "Menor",
    "font_size": 45,
    "position": [20, 20],
    "size": [280, 90],
    "color": [255,0,0]
  }

ENTREGADA = {
    "label": "Entregada",
    "font_size": 45,
    "position": [20, 20],
    "size": [280, 90],
    "color": [0,0,255]
  }


MAYOR = {
    "label": "Mayor",
    "font_size": 45,
    "position": [20, 20],
    "size": [280, 90],
    "color": [0, 255, 0]
  }


pygame.init()
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode(SCR_SIZE)

def load_config(filepath):

    global url
    global color
    global font_size

    print 'Loading config...'
    try:
        with open(filepath) as config_file:
            try:
                config_data = json.load(config_file)
            except ValueError as e:
                print '[FATAL] Error parsing config file: ' + str(e)
                sys.exit(-1)
    except IOError as e:
        print '[FATAL] Error loading config file: ' + str(e)

    config = config_data.get('config', DEFAULT_CONFIG)
    url = config.get('address')

    menor = config_data.get('menor',MENOR)
    color = menor.get('color')
    font_size = menor.get('font_size')



def main(argv):
    filepath = 'config.json'
    if len(argv) > 1:
        filepath = argv[1]
    load_config(filepath)

def espera(text):
    global color
    global font_size

    font = pygame.font.Font(None, font_size)
    label = font.render(str(text), 1, WHITE)
    rect = (0, 0, 300, 100)
    pygame.draw.rect(screen,color,rect)
    screen.blit(label, (30, 30))



if __name__ == "__main__":
    main(sys.argv)

    ser = serial.Serial('/dev/ttyUSB0', BITRATE)
    rfidPattern = re.compile(b'[\W_]+')

    try:
        ser.flushInput()
        ser.flushOutput()
    except Exception, e:
        print "error open serial port: " + str(e)
        exit()

while 1:
    line = ser.readline()
    last_received = line.strip()
    match = rfidPattern.sub('', last_received)
    espera(match)

    pygame.display.update()
