# lightBox Sync
# Basic control of NeoPixels via OSC

use_osc "192.168.1.108", 9090
use_bpm 120

in_thread do
  sync :tick # syncs with unicorn_osc.rb (2 Pi's required for full sync)
  live_loop :lightBox do
    sample :drum_bass_hard
    osc "/rgb", 255, 0, 0
    sleep 1
    sample :drum_bass_hard
    osc "/rgb", 255, 255, 255
    sleep 1
  end
end
