# lightBox Sync (http://callumkirkwood.com/projects/lightBox/)
# Controls RGB LEDs attached to an OSC server
# Send HSV commands for a better range of colour, then convert to RGB at the server side

use_osc "192.168.1.108", 9090
use_bpm 120

in_thread do
  sync :tick # syncs with unicorn_osc.rb, comment out if only using 1 server
  with_fx :reverb, mix: 0.3 do
    live_loop :lightBox do
      sample :drum_bass_soft,  amp: 0.8
      osc "/rgb", 0, 1, 1
      sleep 1
      sample :drum_bass_soft,  amp: 0.8
      osc "/rgb", 0, 0, 1
      sleep 1
    end
  end
end
