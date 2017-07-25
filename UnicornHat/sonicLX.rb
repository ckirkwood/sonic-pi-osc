# SonicLX
# Controls RGB LEDs attached to an OSC server
# Send HSV commands for a better range of colour, then convert to RGB at the server side

use_osc "192.168.1.104", 9090
use_bpm 120

in_thread do
  with_fx :reverb, mix: 0.3 do
    live_loop :unicorn do
      cue :tick
      sample :drum_bass_hard, amp: 0.8
      osc "/rgb", 0, 0, 1
      sleep 1
      sample :drum_bass_hard,  amp: 0.8
      osc "/rgb", 0, 1, 1
      sleep 1
      cue :tock
    end
  end
end
