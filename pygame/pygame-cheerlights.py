#!/usr/bin/env python

import time
import requests
import pygame
from pygame.locals import *

col = "#000000"

#windowSurface = pygame.display.set_mode((800, 600), FULLSCREEN)
windowSurface = pygame.display.set_mode((800, 600), 0,32)
pygame.init()

while True:
    try:
        r = requests.get('http://api.thingspeak.com/channels/1417/field/2/last.json', timeout=2)
        col = r.json()['field2']
    except:
        if col == "#000000":
            col = "#FFFFFF"
        else:
            col = "#000000"
    r, g, b = tuple(ord(c) for c in col[1:].lower().decode('hex'))
    windowSurface.fill((r,g,b))
    pygame.display.update()
    time.sleep(1)
