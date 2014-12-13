import time

def playAnySound():
  file = pickAFile()
  sound = makeSound(file)
  rate = getSamplingRate(sound)
  samples = getLength(sound)
  length = samples/rate
  print length
  
  while (true):
    play(sound)
    time.sleep(length)
  
# 
# Courtesy of freesound.com
# http://www.freesound.org/people/frederic.font/sounds/130878/

