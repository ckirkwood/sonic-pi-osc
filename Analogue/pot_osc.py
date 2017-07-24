# small scale test controlling Sonic Pi with analogue inputs
# requires potSynth.rb running in Sonic Pi 3

import OSC
import threading
import time
import Adafruit_MCP3008
from dotenv import load_dotenv, find_dotenv
import os

# retrieve environment variables
load_dotenv(find_dotenv())
server_ip = os.environ.get('SERVER_IP')
client_ip = os.environ.get('CLIENT_IP')

# set server (listen) and client (send) IPs
receive_address = (server_ip, 22)
send_address = (client_ip, 4559)

# Define pins used by MCP3008
CLK = 11
MISO = 9
MOSI = 10
CS = 8
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

# Initialize the OSC server and the client.
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

# callback functions
def answer_handler(addr, tags, stuff, source):
    print('inside incoming_handler')
    print "---"
    print "received new osc msg from %s" % OSC.getUrlStr(source)
    print stuff

def pot_value():
    while True:
	a = (((mcp.read_adc(0) - 0) * (128 - 0)) / (1023 - 0)) + 0
	b  = (((mcp.read_adc(1) - 0) * (3 - 0)) / (1023 - 0)) + 0
	c = (((mcp.read_adc(2) - 0) * (128 - 0)) / (1023 - 0)) + 0
    	list = [a, b, c]
        send_osc('/pot/value', list)

# Start OSCServer in extra thread
st = threading.Thread( target = s.serve_forever )
st.start()

while True:
    pot_value()
    time.sleep(0.1)
