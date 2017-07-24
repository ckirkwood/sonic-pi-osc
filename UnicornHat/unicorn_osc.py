from OSC import OSCServer
from time import sleep
from threading import Thread
import unicornhat as unicorn
from dotenv import load_dotenv, find_dotenv
import os

unicorn.set_layout(unicorn.PHAT)
unicorn.brightness(0.2)

load_dotenv(find_dotenv())
server_ip = os.environ.get('SERVER_IP')

# functions to call on receipt
def oscInput(addr, tags, stuff, source): 
  print stuff

def all_pixels(addr, tags, stuff, source):
    r, g, b = stuff
    unicorn.clear()
    unicorn.set_all(r, g, b)
    unicorn.show()

# assign server ip and port
server = OSCServer((server_ip, 9090))

# message handlers
server.addDefaultHandlers() #for dealing with unmatched messages 
server.addMsgHandler("/rgb", all_pixels) 

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
