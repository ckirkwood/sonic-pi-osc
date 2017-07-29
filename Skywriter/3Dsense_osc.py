#!/usr/bin/env python

import signal
from sys import exit
import OSC
import time
from dotenv import load_dotenv, find_dotenv
import os
import skywriter

# retrieve environment variables
load_dotenv(find_dotenv())
client_ip = os.environ.get('CLIENT_IP')

# set IP and port of device running Sonic Pi
send_address = (client_ip, 4559)

# Initialize the OSC server and the client.
c = OSC.OSCClient()
c.connect(send_address)

# create function to send message with multiple arguments
def send_osc(addr, *stuff):
    msg = OSC.OSCMessage()
    msg.setAddress(addr)
    for item in stuff:
        msg.append(item)
    c.send(msg)

# Skywriter functions (send OSC messages from each function for a constant stream as you move over the HAT)
some_value = 5000

@skywriter.move()
def move(x, y, z):
    f_x = float("{0:.2f}".format(x)) # reduce output to 2 decimal points
    f_y = float("{0:.2f}".format(y))
    f_z = float("{0:.2f}".format(z))
    print(f_x, f_y, f_z)
    send_osc('/gesture', f_x, f_y, f_z)

@skywriter.flick()
def flick(start,finish):
    print('Got a flick!', start, finish)

@skywriter.airwheel()
def spinny(delta):
    global some_value
    some_value += delta
    if some_value < 0:
        some_value = 0
    if some_value > 10000:
        some_value = 10000
    print('Airwheel:', some_value/100)

@skywriter.double_tap()
def doubletap(position):
    print('Double tap!', position)

@skywriter.tap()
def tap(position):
    print('Tap!', position)

@skywriter.touch()
def touch(position):
    print('Touch!', position)

signal.pause()
