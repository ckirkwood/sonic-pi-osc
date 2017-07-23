# sonicLX
# sends RGB values to an OSC server to control LEDs

use_osc "192.168.1.104", 22
use_bpm 100

loop do
  osc "/rgb/value", 255, 0, 0
  sleep 1
  osc "/rgb/value", 255, 255, 255
  sleep 1
end
