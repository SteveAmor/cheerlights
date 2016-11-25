#!/usr/bin/env python

import time
import requests
from microdotphat import write_string, show

while True:
    try:
        print("Get web request")
        r = requests.get('http://api.thingspeak.com/channels/1417/field/2/last.json')
        col = r.json()['field2']
    except:
        col = " Error!"
    print(col)
    write_string(col, offset_x=-8, kerning=False)
    show()
    time.sleep(1)
