#!/usr/bin/env python

# small scale test controlling Sonic Pi with analogue inputs
# accompanies  potSynth.rb running in Sonic Pi 3

import OSC
import time
import Adafruit_MCP3008
from dotenv import load_dotenv, find_dotenv
import os

# retrieve environment variables
load_dotenv(find_dotenv())
client_ip = os.environ.get('CLIENT_IP')

# set IP and port of device running Sonic Pi
send_address = (client_ip, 4559)

# Initialize the OSC client.
c = OSC.OSCClient()
c.connect(send_address)

# Define pins used by MCP3008
CLK = 11
MISO = 9
MOSI = 10
CS = 8
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

# create a function to send multiple arguments
def send_osc(addr, *stuff):
    msg = OSC.OSCMessage()
    msg.setAddress(addr)
    for item in stuff:
        msg.append(item)
    c.send(msg)

# function to read ADC values and send them to Sonic PI
def pot_value():
    while True:
	a = (((mcp.read_adc(0) - 0) * (128 - 0)) / (1023 - 0)) + 0
	b  = (((mcp.read_adc(1) - 0) * (3 - 0)) / (1023 - 0)) + 0
	c = (((mcp.read_adc(2) - 0) * (128 - 0)) / (1023 - 0)) + 0
    	list = [a, b, c]
        send_osc('/pot/value', list)

# call function on a loop
try:
    while True:
        pot_value()
        time.sleep(0.1)

# clean exit
except KeyboardInterrupt:
    print 'Closing...'
