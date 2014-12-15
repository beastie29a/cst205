# file name: FnalProject.py
# author: Julia Diliberto, Matthew Bozelka, Robert Contreras, Ryan Doherty
# description: CST205 Final Project
#
# Libraries
import time
import threading


#Global variables
  
roomName = ["front yard", "living room", "bedroom", "kitchen", "office","laundry room","back yard","attic"]
roomDirections = ["Go north to enter the house.\n",
                  "Go north to the bedroom, west to the kitchen,\n or south to the front yard\n",
                  "Go south to the living room or west to the office.\n",
                  "Go east to the living room.\n",
                  "Go north to the laundry room or east to the bedroom.\n",
                  "Go south to the office, north to the back yard,\n or up to the attic.\n",
                  "Go south to the laundry room.\n",
                  "Go down to the laundry room.\n"]

roomItems = {
  1 : ['remote control', 'foot stool', 'coffee table'],
  2 : ['baseball bat', 'neck brace', 'halloween wig'],
  3 : ['serrated paring knife', 'butter knife', 'scissors'],
  4 : ['high top chair', 'letter opener', 'stapler'],
  5 : ['laundry detergent', 'hangers', 'iron'],
  6 : ['axe', 'rope', 'wheelbarrow'],
  7 : ['step stool', 'old rifle', 'sword'],
  
}

messages = {
  'already-chosen': 'You have already guessed that item. Try another one or continue.\n',
  'back-in-front' : 'You are back in the front yard and you don\'t have the required items yet! Go back in by going north!\n',
  'won' : 'You did it! You were able to save your friend from hanging!\n',
  'lost' : 'Sorry! Youd didn\'t save your friend in time! Better luck next time!\n',
  'remote control' : 'Why would a remote control ever be useful!\n',
  'foot stool' : 'We need something like this for him to stand on, but this is too small.\n',
  'coffee table' : 'That\'s way too heavy to carry!\n',
  'baseball bat' : 'I don\'t see how that will help.\n',
  'neck brace' : 'You know what! You will need this when we get him down! Nice Choice\n',
  'halloween wig' : 'Why would a halloween ever be useful!\n',
  'scissors' : 'The rope is too thick to cut with scissors!\n',
  'butter knife' : 'hmm.. that\'s way too dull.\n',
  'serrated paring knife' : 'Yes.. that is perfect to cut the rope with.\n',
  'high top chair' : 'This is perfect! Your friend can stand on this while you cut him down.\n',
  'letter opener' : 'I don''t think so. Try again.\n',
  'stapler' : 'Why would a stapler ever be useful!\n',
  'laundry detergent' : 'Why would a laundry degerent ever be useful!\n',
  'hangers' : 'Why would hangers ever be useful!\n',
  'iron' : 'Why would an iron ever be useful!\n',
  'axe' : 'It would take way too long to cut him down with this.\n',
  'rope' : 'I don\'t think you need more rope!\n',
  'wheelbarrow' : 'Maybe it could have helped you carry your items, but all the wheels are flat.\n',
  'step stool' : 'Yes! You can use this to stand on to reach the rope!\n',
  'old rifle' : 'I don\'t think shooting him down is a smart idea!\n',
  'sword' : 'That thing is dull! It\'ll never cut a rope!\n'
}

# items needed to when the game
correctItems = ['Serrated Paring Knife', 'Step Stool', 'High Top Chair', 'Neck Brace']
guessedItems = []


messageDirection = "Which way do you want to go?\n"
messageDirectionError = "Sorry, can't go that way.\n"			

messageIntroduction = """
Welcome to the game \'Don\'t\' Let Me Hang Man!'.
In this game you need to explore the house to find the four items you need to save your friend from hanging!
In each room you will find a list of items to select from.
For every wrong choice your friend will be closer to heanging!
Accepted Commands
Navigation: 'north','south', 'east', 'west','up','down'
Selecting an item: '1', '2', '3' or any other key to continue
Quit Game:  'exit'
Redisplay Instructions: 'help'
"""
					  
messageRoomEntry = "You are in the %s\n"


# Sound items

soundpath = "/Users/rcontreras/code/cst205-final/Sounds/" # Set to root path of github repo

#MODEL
#Business logic goes here



#Take user's input command and currentRoom value
#Reassigns currentRoom to new room value based on
#directional command and return new currentRoom
#currentRoom corresponds to the indexes of the room lists
def moveRoom(inputString,currentRoom):
  if (inputString=="north"):
    currentRoom=currentRoom+1
  elif (inputString=="south"):
    currentRoom=currentRoom-1
  elif (inputString=="west"):
    currentRoom=currentRoom+2
  elif (inputString=="east"):
    currentRoom=currentRoom-2
  elif (inputString=="up"and currentRoom==5):
    currentRoom=7
  elif (inputString=="down"and currentRoom==7):
    currentRoom=5
  return currentRoom


def getRoomInformation(currentRoom):
 return messageRoomEntry % (roomName[currentRoom]) + "\n" +  roomDirections[currentRoom] + "\n" + messageDirection


def inArray(selected, arr):
  for item in arr:
    if selected.lower() == item.lower():
      return true
      
  return false






#VIEW
#User Interface code goes here


def displayRoomInformation(currentRoom):
  printNow(messageRoomEntry % (roomName[currentRoom]))

def displayIntroduction():
  showInformation(messageIntroduction)

def displayMessage(message):
  printNow(message)

def displayItems(Items):
  printNow('There are a few items in this room that might help save your friend!\nItem 1: %s, Item 2: %s, and Item 3: %s \n' % (Items[0], Items[1], Items[2]))



# Sound functions
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









#CONTROLLER
#User interaction code goes here 

def getUserInput(string):
  return requestString(string)
  
def getUserInputForItem():
  return requestString("Select the number of the item you think will help save your friend,\nor any other key to continue\n")



def runGame():

  displayIntroduction()
  
  GameOver = false
  winner = false
  currentRoom = 0
  maxGuesses = 6
  correctGuesses = 0
  incorrectGuesses = 0
  selectedItem = None
  
  inputString=getUserInput(getRoomInformation(currentRoom))
       
  while (inputString<>"exit" and not GameOver): 
    
    if (inputString=="help"):
      displayIntroduction()
      displayRoomInformation(currentRoom)      
      
    else:
      
      if incorrectGuesses == 6:
        winner = false
        GameOver = true
        
      elif correctGuesses == 4:
        winner = true
        GameOver = true
        
      else:
        # the input is correct handle the logic needed
        if (roomDirections[currentRoom].find(inputString.lower())>=0):
          
          currentRoom=moveRoom(inputString,currentRoom)
          displayRoomInformation(currentRoom)
          
          # back in the front yard and have not won. Tell them they they need to go back into the house
          if currentRoom == 0:
            displayMessage(messages['back-in-front'])
        
          # not in the front yard, game isn't over, and the user doesn't have all the items
          else:
            
            if correctGuesses != 4:
              
              pickItem = true
              while pickItem:
          
                displayItems(roomItems[currentRoom])
                selectedItem = getUserInputForItem()
            
                if selectedItem == '1' or selectedItem == '2' or selectedItem == '3': 
                  isCorrect = inArray(roomItems[currentRoom][int(selectedItem) - 1], correctItems)
              
                  # it was a new guessed item
                  if not inArray(roomItems[currentRoom][int(selectedItem) - 1], guessedItems):
                    if isCorrect:
                      # the user guessed a correct item. Anything that gets shown/played while correct goes here
                      correctGuesses += 1
                      guessedItems.append( roomItems[currentRoom][int(selectedItem) - 1] )
                      if correctGuesses == 4:
                        pickItem = false
                      else:
                        displayMessage(messages[roomItems[currentRoom][int(selectedItem) - 1]])
                    else:
                      # the user guessed an incorrect item. Anything that gets shown/played while correct goes here
                      incorrectGuesses += 1
                      guessedItems.append( roomItems[currentRoom][int(selectedItem) - 1] )
                      if incorrectGuesses == 6:
                        pickItem = false
                      else:
                        displayMessage(messages[roomItems[currentRoom][int(selectedItem) - 1]])
              
                  # that was allready guessed
                  else:
                    displayMessage(messages['already-chosen'])
            
                # user has decided to stop guessing and continue searching.
                else:
                  pickItem = false
          
          if incorrectGuesses != 6 and correctGuesses != 4:
            inputString=getUserInput(getRoomInformation(currentRoom))
            
        # incorrect input so redisplay the current room and info
        else:
          displayMessage(messageDirectionError)
          inputString=getUserInput(getRoomInformation(currentRoom))
  
  endGame(winner)      
     

def endGame(winner):
  if winner:
    displayMessage(messages['won'])
  else:
    displayMessage(messages['lost'])
    


def main():
  runGame()

  
