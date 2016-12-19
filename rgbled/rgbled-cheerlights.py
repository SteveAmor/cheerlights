#!/usr/bin/env python

from __future__ import division
import time
import requests
from gpiozero import RGBLED

col = "#000000"

rgbled = RGBLED(17,27,22)

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
    rgbled.color = (r/255, g/255, b/255)
    time.sleep(1)
