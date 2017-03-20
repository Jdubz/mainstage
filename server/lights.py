from dmx import DmxPy
import sys

dmx = DmxPy('/dev/ttyUSB0')

dmx.blackout()

fixture = 18
if sys.argv[1] == '1':
  while fixture > 0:
    chan = fixture * 3
    dmx.setChannel(chan, 20)
    dmx.setChannel(chan-1, 100)
    dmx.setChannel(chan-2, 200)
    fixture -= 1
  print 'turning lights on'
elif sys.argv[1] == '0':
  while fixture > 0:
    chan = fixture * 3
    dmx.setChannel(chan, 0)
    dmx.setChannel(chan-1, 0)
    dmx.setChannel(chan-2, 0)
    fixture -= 1
  print 'turning lights off'

dmx.render()