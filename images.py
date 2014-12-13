
picArms = makePicture('C:\\Users\\GRAM\\Documents\\CST 205\\Final\\picArms.jpg')
picNoArms = makePicture('C:\\Users\\GRAM\\Documents\\CST 205\\Final\\hangman.jpg')
headX = 202
headY = 68




def makeGreen(pic):
  pixels = getPixels(pic)
  for p in pixels:
      r = getRed(p)
      g = getGreen(p)
      b = getBlue(p)
          
      setRed(p, g * .50)
      setGreen(p, g)
      setBlue(p, g * .25)     
  return(pic)

def addTextBoxes(pic,message,chosenItem):
 rect1X = 21
 rect1Y = 87
 rect2X = 21
 rect2Y = 210
 rect1Width = 160
 rect1Height = 70
 rect2Width = 160
 rect2Height = 70
 choiceMessage = 'How is a ' + chosenItem + ' going to help me?'
 mystyle = makeStyle(mono, italic + bold, 14)
 addRectFilled(pic,rect1X,rect1Y,rect1Width,rect1Height, blue)
 addTextWithStyle(pic, rect1X +2, rect1Y+10, message[0:20], mystyle, white)
 addTextWithStyle(pic, rect1X +2, rect1Y+20, message[21:41], mystyle, white)
 if chosenItem != "none":
   addRectFilled(pic,rect2X,rect2Y,rect2Width,rect2Height,blue)
   addTextWithStyle(pic, rect2X +2, rect2Y+10 , choiceMessage[0:19], mystyle, white)
   addTextWithStyle(pic, rect2X + 2, rect2Y+20,choiceMessage[19:29], mystyle, white)
 return pic

def chromakey(pic, backpic):
  newpic = makeEmptyPicture(getWidth(backpic), getHeight(backpic),white)
  copyInto (pic,newpic,headX,headY)
  for x in range (0,getWidth(newpic)):
    for y in range (0,getHeight(newpic)):
      pix = getPixel(newpic,x,y)
      color = getColor(pix)
      if distance(color,white)<10:
        altpix = getPixel(backpic,x,y)
        setColor(pix,getColor(altpix))
  return newpic
  
# Introduction

newpic = addTextBoxes(picArms,introMessage, "none")
introMessage = "Man, you gotta help. Find things in the house to get me down."
show(newpic)

def updatePicStatus(levelOfDestruction, itemChosen):
  face1=makePicture('C:\\Users\\GRAM\\Documents\\CST 205\\Final\\hurt.jpg')  
  deadMessage1 = "You want to see me pushing up daisies?"
  face2=makePicture('C:\\Users\\GRAM\\Documents\\CST 205\\Final\\worried.jpg')
  deadMessage2 = "Come on, Man, I'm gonna be six feet under!"
  face3=makePicture('C:\\Users\\GRAM\\Documents\\CST 205\\Final\\shocked.jpg')
  deadMessage3 = "I'm about to kick the bucket here?!?"
  face4=makePicture('C:\\Users\\GRAM\\Documents\\CST 205\\Final\\sad.jpg')
  deadMessage4 = "Worm food! That's all I have to say"
  face5=makePicture('C:\\Users\\GRAM\\Documents\\CST 205\\Final\\pleading.jpg')
  deadMessage5 = "I'm fading away."
  face6=makePicture('C:\\Users\\GRAM\\Documents\\CST 205\\Final\\last cigarette.jpg')
  deadMessage6 = "My life is passing before my eyes."
  
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
    newpic = addTextBoxes(newpic,deadMessage6,itemChosen)
  show (newpic)
  
  