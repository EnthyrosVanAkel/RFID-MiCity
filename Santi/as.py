import sys
import pygame
import os
import json
import OSC

os.environ["SDL_FBDEV"] = "/dev/fb1"
os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"
os.environ["SDL_MOUSEDRV"] = "TSLIB"

SCR_SIZE = 320, 240
BUTTON_PADDING = 10
WHITE = (255, 255, 255)

DEFAULT_COLORS = {
    'normal': [64, 64, 64],
    'pressed': [127, 127, 127]
}

buttons = []
pressed_button = None

pygame.init()
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode(SCR_SIZE)



def load_config(filepath):
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



    button_layout = config_data.get('buttons', [])
    for button_idx, button_desc in enumerate(button_layout):

        on_press_callbacks = []
        on_release_callbacks = []
        
        text = button_desc.get('label', 'Button')
        font_size = button_desc.get('font_size', 24)
        position = button_desc.get('position', [100, 100])
        size = button_desc.get('size')
        colors = button_desc.get('colors', DEFAULT_COLORS)
        make_button(text, font_size, position, size, colors,
                    on_press_callbacks, on_release_callbacks)


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


def on_mousedown():
    global pressed_button
    click_pos = (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    for button in buttons:
        rect = button['rect']
        if (rect[0] <= click_pos[0] <= rect[0] + rect[2]
                and rect[1] <= click_pos[1] <= rect[1] + rect[3]):
            pressed_button = button
            press_callbacks = button['on_press']
            for callback in press_callbacks:
                callback()
            draw_button(button, True)


def on_mouseup():
    global pressed_button
    if pressed_button is not None:
        draw_button(pressed_button, False)
        release_callbacks = pressed_button['on_release']
        for callback in release_callbacks:
            callback()
        pressed_button = None


def main(argv):
    filepath = 'config.json'
    if len(argv) > 1:
        filepath = argv[1]

    load_config(filepath)


if __name__ == "__main__":
    main(sys.argv)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            on_mousedown()

        if event.type == pygame.MOUSEBUTTONUP:
            on_mouseup()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
    pygame.display.update()
