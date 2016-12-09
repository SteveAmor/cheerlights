#!/usr/bin/env python

import time
import requests
import subprocess

def press(button):
    if "previousButton" not in vars(press):
        press.previousButton = ""
    if(press.previousButton != button):
        press.previousButton = button
        subprocess.call(["irsend", "SEND_ONCE", "CANDLE", button])

press("BTN_1") # Turn on
time.sleep(1)

col = "white"

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
        press("KEY_1")
    elif(col == "green"):
        press("KEY_2")
    elif(col == "blue"):
        press("KEY_3")
    elif(col == "white" or col == "warmwhite" or col == "oldlace"):
        press("KEY_4")
    elif(col == "orange"): # ok, it's not orange but we need something
        press("KEY_6")
    elif(col == "yellow"):
        press("KEY_7")
    elif(col == "purple"):
        press("KEY_9")
    elif(col == "pink"):
        press("KEY_10")
    elif(col == "cyan"):
        press("KEY_11")
    elif(col == "magenta"):
        press("KEY_12")

    time.sleep(1)
