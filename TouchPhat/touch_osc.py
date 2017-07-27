# small scale test controlling Sonic Pi with Pimoroni's Touch  Phat via OSC
# requires touchKeys.rb running in Sonic Pi 3

import OSC
import touchphat
import time
from dotenv import load_dotenv, find_dotenv
import os

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

# confirm script is running by cycling LEDs
def initialise():
    for pad in ['Back','A','B','C','D','Enter']:
        touchphat.set_led(pad, True)
        time.sleep(0.1)
        touchphat.set_led(pad, False)
        time.sleep(0.1)

# callback function
def answer_handler(addr, tags, stuff, source):
    print('inside incoming_handler')
    print "---"
    print "received new osc msg from %s" % OSC.getUrlStr(source)
    print stuff

initialise()

# assign values to touch pads
@touchphat.on_touch(['Back','A','B','C','D','Enter'])
def touch_keys(event):
    if event.name == 'Back':
        send_osc('/touch/trigger', 62)
    elif event.name == 'A':
        send_osc('/touch/trigger', 64)
    elif event.name == 'B':
        send_osc('/touch/trigger', 66)
    elif event.name == 'C':
        send_osc('/touch/trigger', 68)
    elif event.name == 'D':
        send_osc('/touch/trigger', 70)
    elif event.name == 'Enter':
        send_osc('/touch/trigger', 72)

# clean exit
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print 'Closing...'
