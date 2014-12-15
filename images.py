picArmsPath = 'C:\\Users\\GRAM\\Documents\\CST 205\\Final\\Images\\picArms.jpg'
picNoArmsPath = 'C:\\Users\\GRAM\\Documents\\CST 205\\Final\\Images\\hangman.jpg'
picArms = makePicture(picArmsPath)
picNoArms = makePicture(picNoArmsPath)
newPic = makeEmptyPicture(getWidth(picArms), getHeight(picArms),white)
currentPic =  makeEmptyPicture(getWidth(picArms), getHeight(picArms),white)

def yellowToGreen(pic):
# Takes a picture as input
# Makes yellow pixels green
# Returns the picture
  pixels = getPixels(pic)
  for p in pixels:
    if distance(getColor(p),yellow) < 150:
      r = getRed(p)
      g = getGreen(p)
      b = getBlue(p)          
      setRed(p, g * .50)
      setGreen(p, g)
      setBlue(p, g * .25)     
  return(pic)

def addTextBoxes(pic,message,chosenItem):
# Takes a picture and two strings as input
# Add two textboxes with a message in each
# Returns the new picture
 rect1X = 11 # X coordinate of first rectangle
 rect1Y = 87 # Y coordinate of first rectangle
 rect2X = 11 # X coordinate of second rectangle
 rect2Y = 210 # Y coordinate of second rectangle
 rect1Width = 180 # width of first rectangle
 rect1Height = 70 # height of first rectangle
 rect2Width = 180 # width of first rectangle
 rect2Height = 70 # height of first rectangle
 choiceMessage = 'How is a ' + chosenItem # first line of second textbox message
 choiceMessage2 = 'going to help me?' # second line of second textbox message
 mystyle = makeStyle(mono, italic + bold, 14) # style for text in boxes
 addRectFilled(pic,rect1X,rect1Y,rect1Width,rect1Height, red) # first textbox
 addTextWithStyle(pic, rect1X +2, rect1Y+10, message[0:21], mystyle, white) # first line, first textbox
 addTextWithStyle(pic, rect1X +2, rect1Y+30, message[21:42], mystyle, white) # second line, first textbox
 addTextWithStyle(pic, rect1X +2, rect1Y+50, message[42:60], mystyle, white) # third line, first textbox
 if chosenItem != "none":
   addRectFilled(pic,rect2X,rect2Y,rect2Width,rect2Height,red) # second textbox
   addTextWithStyle(pic, rect2X +2, rect2Y+10 , choiceMessage, mystyle, white) # first line, second textbox
   addTextWithStyle(pic, rect2X + 2, rect2Y+30,choiceMessage2, mystyle, white) # second line, second textbox
 return pic

def chromakey(face, backPic):
  headX = 202 # X coordinate of face
  headY = 68 # Y coordinate of face
  newPic = makeEmptyPicture(getWidth(backPic), getHeight(backPic),white)
  copyInto (face,newPic,headX,headY)
  for x in range (0,getWidth(newPic)):
    for y in range (0,getHeight(newPic)):
      pix = getPixel(newPic,x,y)
      color = getColor(pix)
      if distance(color,white)<10:
        altpix = getPixel(backPic,x,y)
        setColor(pix,getColor(altpix))
  return newPic
  
def initialPic (currentPic):
# Takes newPic as input
# Fills and displays newPic to represent inital status

  face = makePicture('C:\\Users\\GRAM\\Documents\\CST 205\\Final\\Images\\worried.jpg')
  introMessage = "Man, you gotta help. Go look in the house. Find some tools."
  newPic = chromakey(face,picNoArms)
  newPic = addTextBoxes(newPic,introMessage, "none", currentPic)

  show(newPic)

def updatePicStatus(incorrectGuesses, selectedItem):
# Updates the picture to reflect the number of mistakes made so far

# Face file paths
  face1Path = 'C:\\Users\\GRAM\\Documents\\CST 205\\Final\\Images\\hurt.jpg'
  face2Path = 'C:\\Users\\GRAM\\Documents\\CST 205\\Final\\Images\\question.jpg'
  face3Path = 'C:\\Users\\GRAM\\Documents\\CST 205\\Final\\Images\\shocked.jpg'
  face4Path = 'C:\\Users\\GRAM\\Documents\\CST 205\\Final\\Images\\sad.jpg'
  face5Path = 'C:\\Users\\GRAM\\Documents\\CST 205\\Final\\Images\\pleading.jpg'
  face6Path = 'C:\\Users\\GRAM\\Documents\\CST 205\\Final\\Images\\last cigarette.jpg'
  face1=makePicture(face1Path)  
  deadMessage1 = "Do you want to see me pushing up daisies?"
  face2=makePicture(face2Path)
  deadMessage2 = "Come on, I'm gonna be six feet under!"
  face3=yellowToGreen(makePicture(face3Path))
  deadMessage3 = "I'm about to kick the bucket here?!?"
  face4=makePicture(face4Path)
  deadMessage4 = "Worm food! That's all I have to say"
  face5=makePicture(face5Path)
  deadMessage5 = "I'm fading away."
  face6=makePicture(face6Path)
  deadMessage6 = "That's it. I'm riding the white horse."
 
  if incorrectGuesses == 1:
    newPic = chromakey(face1,picArms)
    newPic = addTextBoxes(newpic,deadMessage1,selectedItem)
  elif incorrectGuesses == 2:
    newPic = chromakey(face2,picNoArms)
    newPic = addTextBoxes(newPic,deadMessage2,selectedItem)
  elif incorrectGuesses == 3:
    newPic = chromakey(face3,picArms)
    newPic = addTextBoxes(newPic,deadMessage3,selectedItem)
  elif incorrectGuesses == 4:
    newPic = chromakey(face4,picNoArms)   
    newPic =  addTextBoxes(newPic,deadMessage4,selectedItem)
  elif incorrectGuesses == 5:
    newPic = chromakey(face5,picArms)
    newPic = addTextBoxes(newPic,deadMessage5,selectedItem)
  elif incorrectGuesses == 6:
    newPic = chromakey(face6,picArms)
    newPic = addTextBoxes(newpic,deadMessage6,"none")
  show (newPic)
  return newPic
  