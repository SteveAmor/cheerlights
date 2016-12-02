#!/usr/bin/env python

import time
import requests
import subprocess

col = "white"

subprocess.call(["irsend", "SEND_ONCE", "CANDLE", "BTN_1"])

while True:
    try:
        r = requests.get('http://api.thingspeak.com/channels/1417/field/1/last.json')
        col = r.json()['field1']
    except:
        if col == "white":
            col = "red"
        else:
            col = "white"

    if(col == "red"):
        subprocess.call(["irsend", "SEND_ONCE", "CANDLE", "KEY_1"])
    elif(col == "green"):
        subprocess.call(["irsend", "SEND_ONCE", "CANDLE", "KEY_2"])
    elif(col == "blue"):
        subprocess.call(["irsend", "SEND_ONCE", "CANDLE", "KEY_3"])
    elif(col == "white" or col == "warmwhite" or col == "oldlace"):
        subprocess.call(["irsend", "SEND_ONCE", "CANDLE", "KEY_4"])
    elif(col == "orange"): # ok, it's not orange but we need something
        subprocess.call(["irsend", "SEND_ONCE", "CANDLE", "KEY_6"])
    elif(col == "yellow"):
        subprocess.call(["irsend", "SEND_ONCE", "CANDLE", "KEY_7"])
    elif(col == "purple"):
        subprocess.call(["irsend", "SEND_ONCE", "CANDLE", "KEY_9"])
    elif(col == "pink"):
        subprocess.call(["irsend", "SEND_ONCE", "CANDLE", "KEY_10"])
    elif(col == "cyan"):
        subprocess.call(["irsend", "SEND_ONCE", "CANDLE", "KEY_11"])
    elif(col == "megenta"):
        subprocess.call(["irsend", "SEND_ONCE", "CANDLE", "KEY_12"])
    time.sleep(1)
