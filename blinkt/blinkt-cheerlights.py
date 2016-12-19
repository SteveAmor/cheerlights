#!/usr/bin/env python

import time
import requests
from blinkt import set_pixel, show

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
    for i in range(8):
        set_pixel(i, r, g, b)
    show()
    time.sleep(1)
