import time
import threading

path = "/Users/rcontreras/code/cst205-final/Sounds/" # Set to root path of github repo

#
# Game play music, need to figure out way to call function in the background
def backgroundMusic():
  file = path + 'background.wav'
  sound = makeSound(file)
  rate = getSamplingRate(sound)
  samples = getLength(sound)
  length = samples/rate
  print length
  
  while (true):
    play(sound)
    time.sleep(length)

# Example of how background sound can be called in a separate thread in the background
#music_thread = threading.Thread(target=backgroundMusic)
#music_thread.start()
#  Have not found a way to stop the thread

# Functino to play sound when entering a room
def enterRoomSound(room):
  if room == 'front yard':
    soundLibrary('doorclose')
  elif room == 'living room':
   soundLibrary('doorclose')
  elif room == 'bedroom':
   soundLibrary('doorclose')
  elif room == 'kitchen':
   soundLibrary('doorclose')
  elif room == 'office':
   soundLibrary('doorclose')
  elif room == 'laundry room':
   soundLibrary('stairs')
  elif room == 'back yard':
   soundLibrary('doorclose')
  elif room == 'attic':
   soundLibrary('stairs')
  
  
# Finction to play sound when obtaining item
def itemSound(item):
  if item == 'ladder':
    soundLibrary('dong')
  elif item == 'scissors':
    soundLibrary('plock')
    
def soundLibrary( sound ):
  file = path + sound + '.wav'
  sound = makeSound(file)
  play(sound)

# Function to combine sounds and playthem at the end when freeing your friend
def combineSounds():
  return true
  
def helpMeSound():
  soundLibrary('help')
  
# 
# Sound files courtesy of freesound.com
# http://www.freesound.org/people/frederic.font/sounds/130878/

