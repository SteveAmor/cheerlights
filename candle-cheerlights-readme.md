# Mood Candle Cheerlights

![Candles](/images/candles.jpg)

## Introduction

Mood candles are available in high street stores (Lakeland for example) and on eBay.  They have a simple infrared remote control that looks likes this:

![Remote Control](/images/remote.jpg)

In this project, the remote control has been replaced by a Raspberry Pi running lirc to change the colour of the candles based on the latest Cheerlights colour.

![Raspberry Pi](/images/pi.jpg)

## Installing lirc

This is how I got ```irsend``` working using a fresh install of Raspian Jessie 2016-11-25

```
cd
sudo apt-get update
sudo apt-get install lirc
git clone https://github.com/steveamor/cheerlights.git
sudo cp ~/cheerlights/lircd.conf /etc/lirc/
```

Update ```/etc/rc.local``` with the following three lines before ```exit 0```

```
ln -s /dev/lirc0 /dev/lirc # this is the hack that fixes the "hardware does not support sending" error
lircd &
python /home/pi/cheerlights/candle-cheerlights.py &
```

Ensure ```/boot/config.txt``` has the following line in it

```
dtoverlay=lirc-rpi,gpio_out_pin=14
```

Ensure ```/etc/lirc/hardware.conf``` contains the following

```
LIRCD_ARGS="--uinput"
#START_LIRCMD=false
#START_IREXEC=false
LOAD_MODULES=true
DRIVER="default"
DEVICE="/dev/lirc0"
MODULES="lirc_rpi"
LIRCD_CONF=""
LIRCMD_CONF=""
```

##Hardware

* Raspberry Pi.
* IR LED (5mm 940nm).
* 330 ohm resistor (0.25 watt).

Long leg of IR LED to 330ohm resistor to GPIO14

Short leg of IR LED to GND

