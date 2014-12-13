picArms = makePicture('C:\\Users\\GRAM\\Documents\\CST 205\\Final\\picArms.jpg')
picNoArms = makePicture('C:\\Users\\GRAM\\Documents\\CST 205\\Final\\hangman.jpg')

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

def chromakey(face, backpic):
  headX = 202 # X coordinate of face
  headY = 68 # Y coordinate of face
  newpic = makeEmptyPicture(getWidth(backpic), getHeight(backpic),white)
  copyInto (face,newpic,headX,headY)
  for x in range (0,getWidth(newpic)):
    for y in range (0,getHeight(newpic)):
      pix = getPixel(newpic,x,y)
      color = getColor(pix)
      if distance(color,white)<10:
        altpix = getPixel(backpic,x,y)
        setColor(pix,getColor(altpix))
  return newpic
  
# Inital status
face = makePicture('C:\\Users\\GRAM\\Documents\\CST 205\\Final\\worried.jpg')
newpic = chromakey(face,picNoArms)
newpic = addTextBoxes(newpic,introMessage, "none")
introMessage = "Man, you gotta help. Go look in the house. Find some tools."
show(newpic)

def updatePicStatus(levelOfDestruction, itemChosen):
# Updates the picture to reflect the number of mistakes made so far
  face1=makePicture('C:\\Users\\GRAM\\Documents\\CST 205\\Final\\hurt.jpg')  
  deadMessage1 = "Do you want to see me pushing up daisies?"
  face2=makePicture( 'C:\\Users\\GRAM\\Documents\\CST 205\\Final\\question.jpg')
  deadMessage2 = "Come on, I'm gonna be six feet under!"
  face3=yellowToGreen(makePicture('C:\\Users\\GRAM\\Documents\\CST 205\\Final\\shocked.jpg'))
  deadMessage3 = "I'm about to kick the bucket here?!?"
  face4=makePicture('C:\\Users\\GRAM\\Documents\\CST 205\\Final\\sad.jpg')
  deadMessage4 = "Worm food! That's all I have to say"
  face5=makePicture('C:\\Users\\GRAM\\Documents\\CST 205\\Final\\pleading.jpg')
  deadMessage5 = "I'm fading away."
  face6=makePicture('C:\\Users\\GRAM\\Documents\\CST 205\\Final\\last cigarette.jpg')
  deadMessage6 = "That's it. I'm riding the white horse."
 
  if levelOfDestruction == 1:
    newpic = chromakey(face1,picArms)
    newpic = addTextBoxes(newpic,deadMessage1,itemChosen)
  elif levelOfDestruction == 2:
    newpic = chromakey(face2,picNoArms)
    newpic = addTextBoxes(newpic,deadMessage2,itemChosen)
  elif levelOfDestruction == 3:
    newpic = chromakey(face3,picArms)
    newpic = addTextBoxes(newpic,deadMessage3,itemChosen)
  elif levelOfDestruction == 4:
    newpic = chromakey(face4,picNoArms)   
    newpic =  addTextBoxes(newpic,deadMessage4,itemChosen)
  elif levelOfDestruction == 5:
    newpic = chromakey(face5,picArms)
    newpic = addTextBoxes(newpic,deadMessage5,itemChosen)
  elif levelOfDestruction == 6:
    newpic = chromakey(face6,picArms)
    newpic = addTextBoxes(newpic,deadMessage6,"none")
  show (newpic)
  
  