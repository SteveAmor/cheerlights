#!/usr/bin/env python

import time
import requests
import scrollphat

while True:
    try:
        r = requests.get('http://api.thingspeak.com/channels/1417/field/1/last.json', timeout=2)
        col = r.json()['field1']
    except:
        col = "Error!"

    scrollphat.clear()
    scrollphat.write_string(col,11)
    length = scrollphat.buffer_len()
    for i in range(length):
        scrollphat.scroll()
        time.sleep(0.1)
