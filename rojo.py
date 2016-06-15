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
URL = 'http://papalote.cocoplan.mx/v0/visitante'
SCR_SIZE = 320, 240
WHITE = (255, 255, 255)

pygame.init()
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode(SCR_SIZE)



def make_button(text, font_size, position, size, colors, on_press, on_release):
    font = pygame.font.Font(None, font_size)
    label = font.render(str(text), 1, WHITE)
    x = position[0]
    y = position[1]
    if size is None:
        width = label.get_width()
        height = label.get_height()
        rect = (x - BUTTON_PADDING, y - BUTTON_PADDING,
                width + BUTTON_PADDING * 2, height + BUTTON_PADDING * 2)
    else:
        width = size[0]
        height = size[1]
        rect = (x, y, width, height)

    button = {
        'label': label,
        'normal_color': (colors.get('normal', DEFAULT_COLORS['normal'])),
        'pressed_color': (colors.get('pressed', DEFAULT_COLORS['pressed'])),
        'rect': rect,
        'center': True if size else False,
        'on_press': on_press,
        'on_release': on_release
    }
    buttons.append(button)
    draw_button(button, False)


def draw_button(desc, pressed):
    color = desc['pressed_color' if pressed else 'normal_color']
    rect = desc['rect']
    label = desc['label']
    center = desc['center']
    x = rect[0]
    y = rect[1]
    width = rect[2]
    height = rect[3]
    label_width = label.get_width()
    label_height = label.get_height()
    pygame.draw.rect(screen, color, rect)
    label_x = x + (width - label_width) / 2.0 if center \
        else (x + BUTTON_PADDING)
    label_y = y + (height - label_height) / 2.0 if center \
        else (y + BUTTON_PADDING)
    screen.blit(label, (label_x, label_y))



    

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
        data = {'rfid':decimal,'zona':1,'experiencia':1}
        r = requests.get(URL,params = data)
        json = r.json()
        edad = json.get('edad')
        if (edad < '18'):
            print 'No permitido'
        else:
            print 'Permitido'
            
        buffer = ''
        lines = ''

        pygame.display.update()
