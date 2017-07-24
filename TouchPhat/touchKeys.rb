# touchKeys
# Requires a Raspberry Pi w/ Pimoroni Touch Phat
# Client code: touch_osc.py

live_loop :touch do
  use_real_time
  a, b, c = sync '/osc/touch/trigger'
  synth :prophet, note: a
end
