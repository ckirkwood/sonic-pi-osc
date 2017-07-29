# 3D Synth
# Takes 3D gestures from a Skywriter HAT as input
# Client: 3Dsense_osc.py

use_real_time

# round incoming coordinates down to 2 decimal places
define :get_xyz do
  x, y, z = sync '/osc/gesture'
  $a = x.round(2)
  $b = y.round(2)
  $c = z.round(2)
end

loop do
  get_xyz
  synth :tri, note: $a*127, amp: $c
end
