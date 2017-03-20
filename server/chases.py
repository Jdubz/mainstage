from dmx import DmxPy
import sys
import time

chaseNum = sys.argv[1]

frame = 10.
countUp = True
frameLoop = 44. * 15.
framerate = 1000./44./100.0

dmx = DmxPy('/dev/ttyUSB0')
dmx.blackout()

while True:
  fixtures = 18
  if chaseNum == '1':
    while fixtures > 0:
      chan = fixtures * 3

      if fixtures % 3 == 0:
        dmx.setChannel(chan-2, int((frame/frameLoop)*120.))
        dmx.setChannel(chan, int((frame/frameLoop)*120.))
      elif fixtures % 3 == 1:
        fix2 = frameLoop - frame
        dmx.setChannel(chan-2, int(((fix2/frameLoop)*30.)+60.))
        dmx.setChannel(chan-1, int((fix2/frameLoop)*30))
        dmx.setChannel(chan, int(((fix2/frameLoop)*30.)+60.))
      elif fixtures % 3 == 2:
        if frame > frameLoop / 2:
          fix3 = frameLoop - frame
        else:
          fix3 = frame
        dmx.setChannel(chan-2, int((fix3 /(frameLoop/2))*30.))
        dmx.setChannel(chan, int((fix3 /(frameLoop/2))*30.))

      fixtures -= 1

  elif chaseNum == '2':
    while fixtures > 0:
      chan = fixtures * 3
      if fixtures % 3 == 0:
        dmx.setChannel(chan-2, int((frame/frameLoop)*120.))
        dmx.setChannel(chan, int((frame/frameLoop)*120.))
      elif fixtures % 3 == 1:
        fix2 = frameLoop - frame
        dmx.setChannel(chan-2, int(((fix2/frameLoop)*30.)+60.))
        dmx.setChannel(chan-1, int((fix2/frameLoop)*30))
      elif fixtures % 3 == 2:
        if frame > frameLoop / 2:
          fix3 = frameLoop - frame
        else:
          fix3 = frame
        dmx.setChannel(chan-2, int((fix3 /(frameLoop/2))*30.))

      fixtures -= 1

  if countUp:
    frame += 1
    if frame == frameLoop:
        countUp = False
  else:
    frame -= 1
    if frame == 10:
        countUp = True

  dmx.render()
  time.sleep(framerate/1000.)