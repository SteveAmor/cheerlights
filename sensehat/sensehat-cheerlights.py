#!/usr/bin/env python

import time
import requests
from sense_hat import SenseHat

sense = SenseHat()

col = "#000000"

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
    sense.clear(r,g,b)
    time.sleep(1)
