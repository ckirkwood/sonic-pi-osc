# small scale test controlling Pimoroni's Unicorn Phat with OSC commands from Sonic Pi
# requires sonicLX.rb running in Sonic Pi 3

import OSC
import threading
import unicornhat as unicorn
from dotenv import load_dotenv, find_dotenv
import os

unicorn.set_layout(unicorn.PHAT)

# retrieve environment variables
load_dotenv(find_dotenv())
server_ip = os.environ.get('SERVER_IP')
client_ip = os.environ.get('CLIENT_IP')

# set server (listen) and client (send) IPs
receive_address = (server_ip, 22)
send_address = (client_ip, 4559)

# initialize the OSC server and the client.
s = OSC.OSCServer(receive_address)
c = OSC.OSCClient()
c.connect(send_address)

# send function for multiple arguments
def send_osc(addr, *stuff):
    msg = OSC.OSCMessage()
    msg.setAddress(addr)
    for item in stuff:
        msg.append(item)
    c.send(msg)

# simple callback functions
def answer_handler(addr, tags, stuff, source):
    print('inside incoming_handler')
    print "---"
    print "received new osc msg from %s" % OSC.getUrlStr(source)
    print stuff

def all_pixels(addr, tags, stuff, source):
    print('inside incoming_handler')
    print "---"
    print "received new osc msg from %s" % OSC.getUrlStr(source)
    while True:
        r, g, b = stuff
        unicorn.clear()
        unicorn.set_all(r, g, b)
        unicorn.show()

# Start OSCServer in extra thread
st = threading.Thread( target = s.serve_forever )
st.start()
# adding callback functions to listener
s.addMsgHandler("/rgb/value", all_pixels)
