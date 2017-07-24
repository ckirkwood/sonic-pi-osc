# SonicLX
# sends RGB values to an OSC server and syncs with a second server w/ NeoPixels

use_osc "192.168.1.104", 9090
use_bpm 120

live_loop :unicorn do
  cue :tick
  sample :drum_bass_hard
  osc "/rgb", 255, 255, 255
  sleep 1
  sample :drum_bass_hard
  osc "/rgb", 255, 0, 0
  sleep 1
end
