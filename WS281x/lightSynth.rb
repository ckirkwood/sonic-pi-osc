# lightSynth
# midi/note_on triggers OSC commands to NeoPixels, with saturation modified by velocity

use_osc "192.168.1.108", 9090
use_bpm 120
use_real_time


in_thread do
  live_loop :keys do
    with_fx :tremolo do |t|
      note, velocity = sync "/midi/mpkmini2/0/2/note_on"
      synth :tri, note: note, amp: velocity / 127.0
      osc "/rgb", note/2, note*2, velocity # switch order to change hue
    end
  end
end
