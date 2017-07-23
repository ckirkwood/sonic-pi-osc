# potSynth
# requires a Raspberry Pi with analogue inputs (i.e. http://callumkirkwood.com/projects/potHat/)
# Client: pot_osc.py

live_loop :potSynth do
  use_real_time
  a, b, c = sync '/osc/pot/value'
  synth :tb303, note: a, wave: b, pulse_width: (c/158.75)+0.1, sustain: 0.5
  sleep 0.1
end
