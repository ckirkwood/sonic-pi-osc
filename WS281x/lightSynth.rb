# lightSynth
# midi/note_on triggers OSC commands to NeoPixels, with saturation modified by velocity
# send HSV values for a better range of colour, then convert to RGB at the server side

use_osc "192.168.1.108", 9090
use_bpm 120


in_thread do
  live_loop :keys do
    with_fx :tremolo do |t|
      use_real_time
      note, velocity = sync "/midi/mpkmini2/0/2/note_on"
      synth :tri, note: note, amp: velocity / 127.0
      n = note / 100.0
      osc "/rgb", n, 1, 1
    end
  end
end
