from OSC import OSCServer
from time import sleep
from threading import Thread
from dotenv import load_dotenv, find_dotenv
from neopixel import *
import signal
import sys
import os

# LED strip configuration:
LED_COUNT      = 48
LED_PIN        = 18
LED_FREQ_HZ    = 800000
LED_DMA        = 5
LED_BRIGHTNESS = 255
LED_INVERT     = False

# Create NeoPixel object, initialise library
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT)
strip.begin()

load_dotenv(find_dotenv())
server_ip = os.environ.get('SERVER_IP')

# base neo pixel functions
def signal_handler(signal, frame):
    colorWipe(strip, Color(0,0,0))
    sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

def colorWipe(strip, color):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()

# functions called by message handlers
def oscInput(addr, tags, stuff, source):
    print stuff

def lightBox(addr, tags, stuff, source):
    r, b, g = stuff
    print stuff
    colorWipe(strip, Color(b, r, g))

# assign server ip and port
server = OSCServer((server_ip, 9090))

# message handlers
server.addDefaultHandlers() #for dealing with unmatched messages
server.addMsgHandler("/rgb", lightBox)

# start thread
server_thread= Thread(target= server.serve_forever)
server_thread.daemon= True
server_thread.start()

# clean exit
try:
    while True:
      sleep(1)
except KeyboardInterrupt:
    print 'done'
    server.close()
