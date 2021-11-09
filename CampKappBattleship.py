import turtle as t
import tkinter as tk
fontSettings=("Arial",40,"underline","bold")
title="BATTLESHIP"
dirTitle="Directions"
directions="""1) Choose which version of the game you want
    to play. 

2a) Use your keyboard to say where you would like 
    to place your pieces (EX: Type A4 to put your piece in A4)

2b) Use the arrow keys to put the ship in 

3) Input the coordinates of where you want to
    attack (ex: A3)

4) Press the button to launch the attack"""

credits="""1)Biggo Boi's Games (Creators of Meme Madness)

2) Mason Camp- 
Main Menu, Directions, Credits, keyboard inputs, 
switching screens, graphic drawer

3) Bryce Kapp-
 Movement of pieces, placing pieces,
  switching players, gameboard, hit detection
"""

#defined variables for the board
hasBothPlayerPlaceThereShipsDown=False
battleshipPiecesTurList=[]
player1BattleshipPiecesCoordinates=[]
player2BattleshipPiecesCoordinates=[]
player1HitCoordinatesList=[]
player1MissCoordinatesList=[]
player2HitCoordinatesList=[]
player2MissCoordinatesList=[]
shipList=["carrier","battleship","cruiser","submarine","destroyer"]
player1ShipList=shipList
player2ShipList=shipList
shipSizeList=[5,4,3,3,2]
shipListIndex=0
shipSizeListIndex=0
player="1"

#start of Camp Portion
#main menu screen
wn=t.Screen()
wn.bgcolor("SkyBlue")
wn.setup(height=500,width=500)

"""def shipPlacer():
  piecePlacer=t.Turtle("square")
  piecePlacer.turtlesize(1.8)"""

#clears the main screen
def mainScreenClear():
  #clears screen
  wn.clearscreen()
  #opens the directions page
  directionsPage()

#opens the PvP gamemode
def openPvP():
  #clears screen
  wn.clearscreen()
  #opens the draw board function
  playGame()

#opens the credits
def openCredits():
  wn.clearscreen()
  creditMaker()

#creates the main menu
def menu():
  # this is a seperate screen for when you clear 
  menuScreen=t.Screen()
  menuScreen.bgcolor("SkyBlue")
  menuScreen.setup(height=500,width=500)
  #Writes the title for the gameboard
  titleWriter=t.Turtle(visible=False)
  titleWriter.penup()
  titleWriter.setposition(-180,130)
  titleWriter.write(title,font=fontSettings)

  #places the PvP button
  pvpButton=t.Turtle("square",visible=False)
  pvpButton.turtlesize(1,1)
  pvpButton.penup()
  pvpButton.goto(0,25)
  pvpButton.write("Player Vs. Player- to access press 1",align="center",font=("Arial",12,"underline"))

  #makes the Directions button
  directionsButton=t.Turtle("square",visible=False)
  directionsButton.turtlesize(2,10)
  directionsButton.penup()
  directionsButton.setposition(0,0)
  directionsButton.write("Directions- To access press 2",align="center",font=("Arial",12,"underline"))

  # makes the Credits Button
  creditsBTN=t.Turtle(visible=False)
  creditsBTN.penup()
  creditsBTN.setposition(0,-25)
  creditsBTN.write("Credits- To access press 3",align="center",font=("Arial",12,"underline"))

  #draws the little ship at the bottom
  shipDrawer=t.Turtle(visible=False)
  shipDrawer.speed(0)
  shipDrawer.fillcolor("Grey")

  shipDrawer.penup()
  shipDrawer.goto(10,-235)
  shipDrawer.pendown()
  shipDrawer.begin_fill()

  shipDrawer.forward(125)
  shipDrawer.left(60)
  shipDrawer.forward(60)
  shipDrawer.left(120)

  shipDrawer.forward(50)
  shipDrawer.right(90)
  shipDrawer.forward(35)
  shipDrawer.left(90)
  shipDrawer.forward(50)
  shipDrawer.left(90)
  shipDrawer.forward(35)

  shipDrawer.right(90)
  shipDrawer.forward(260)
  shipDrawer.back(10)

  shipDrawer.left(120)
  shipDrawer.forward(60)
  shipDrawer.left(60)
  shipDrawer.forward(235)
  shipDrawer.end_fill()

  #onkeypresses for menuScreen
  menuScreen.onkeypress(mainScreenClear,"2")
  menuScreen.onkeypress(openPvP,"1")
  menuScreen.onkeypress(openCredits,"3")
  menuScreen.listen()

  menuScreen.mainloop()

def directionsPage():
  global menu
  #seperate screen for the directions page
  directScreen=t.Screen()
  directScreen.bgcolor("SkyBlue")
  directScreen.setup(height=500,width=500)

  #writes the word DIRECTIONS at the top
  dirTitleWriter=t.Turtle(visible=False)
  dirTitleWriter.penup()
  dirTitleWriter.setposition(-160,130)
  dirTitleWriter.write(dirTitle,font=fontSettings)

  #writes out the directions
  directionsWriter=t.Turtle(visible=False)
  directionsWriter.penup()
  directionsWriter.setposition(-200,-130)
  directionsWriter.write(directions,font=("Arial",13))

  #creates the back button
  backTurtle=t.Turtle(visible=False)
  backTurtle.penup()
  backTurtle.setposition(-150,210)
  backTurtle.write("EXIT-press e to leave",align="center",font=("Arial",11,"bold"))

  #the function to leave the directions and return to the main menu
  def leaveDirections():
    directScreen.clearscreen()
    menu()

  #the onkeypress to call leaveDirection
  directScreen.onkeypress(leaveDirections,"e")

  directScreen.mainloop()

#start of Kapp portion
def playGame():
  global hasBothPlayerPlaceThereShipsDown,battleshipPiecesTurList,player1BattleshipPiecesCoordinates,player2BattleshipPiecesCoordinates,player1HitCoordinatesList,player1MissCoordinatesList,player2HitCoordinatesList,player2MissCoordinatesList,shipList,player1ShipList,player2ShipList,shipSizeList,shipListIndex,shipSizeListIndex,player
  #creates the boardgame screen
  board=t.Screen()  
  letterLableWriter=t.Turtle(visible=False)
  letterLableWriter.speed(0)
  letterLableWriter.penup()
  letterLableWriter.color("skyblue")
  numberLableWiter=t.Turtle(visible=False)
  numberLableWiter.speed(0)
  numberLableWiter.penup()
  numberLableWiter.color("skyblue")
  fontSetting=("Arial",16,"normal")
  winFontSetting=("Arial",40,"normal")

  #creates the input box
  def popUpMenu():
      global txtBox,infoLable,popUpScreen,hasBothPlayerPlaceThereShipsDown
      popUpScreen=tk.Tk()
      '''battleshipPiecesTurList.clear()'''
      '''print(battleshipPiecesTurList)'''
      frame=tk.Frame(popUpScreen)
      frame.pack()
      txtBox=tk.Entry(frame)
      txtBox.pack()
      if hasBothPlayerPlaceThereShipsDown==False:
        infoLable=tk.Label(frame,text=f"Player {player} type in the coordinate you what to place the {shipList[0]} and the size is {shipSizeList[0]}.\nAfter you click the button then use the arrow keys to control the ship placement direction.")
      else:
          infoLable=tk.Label(frame,text=f"Player {player} type in the coordinate you want to target.")
      infoLable.pack()
      placementButton=tk.Button(frame,command=checkDirectionPlacement)
      placementButton.pack()
  #function to check the placement
  def checkDirectionPlacement():
      global txtBox,row,currentX,currentY,popUpScreen,hasBothPlayerPlaceThereShipsDown
      inputData=txtBox.get()
      if len(inputData)==2:
          row=inputData[0]
          column=inputData[1]
          column=int(column)-1
      elif len(inputData)==3:
          row=inputData[0]
          column=inputData[1]+inputData[2]
          column=int(column)-1
      print("row=",row)
      print("column=",column)
      print(inputData)
      if row=="A" or row=="a":
          row=0
      elif row=="B" or row=="b":
          row=1
      elif row=="C" or row=="c":
          row=2
      elif row=="D" or row=="d":
          row=3
      elif row=="E" or row=="e":
          row=4
      elif row=="F" or row=="f":
          row=5
      elif row=="G" or row=="g":
          row=6
      elif row=="H" or row=="h":
          row=7
      elif row=="I" or row=="i":
          row=8
      elif row=="J" or row=="j":
          row=9
      battleshipPiecesTur=t.Turtle("square",visible=False)
      battleshipPiecesTur.speed(0)
      battleshipPiecesTur.penup()
      battleshipPiecesTur.goto(-289+65*column,300-65*row)
      currentX=battleshipPiecesTur.xcor()
      currentY=battleshipPiecesTur.ycor()
      if hasBothPlayerPlaceThereShipsDown==True:
          hitDetection()
      else:
          wn.onkeypress(placeShipToTheRight,"Right")
          wn.onkeypress(placeShipToTheLeft,"Left")
          wn.onkeypress(placeShipUp,"Up")
          wn.onkeypress(placeShipDown,"Down")
          wn.listen()
  #function to place the ship to the right
  def placeShipToTheRight():
      global row,currentX,currentY,shipListIndex,shipSizeList,shipSizeListIndex,infoLable,popUpScreen,player
      shipSize=shipSizeList[shipSizeListIndex]
      needBreak=False
      battleshipPiecesTur=t.Turtle("square",visible=False)
      battleshipPiecesTur.speed(0)
      battleshipPiecesTur.penup()
      battleshipPiecesTur.shapesize(3)
      battleshipPiecesTur.color("gray")
      amountToRemoveFromList=0
      shipSizeListIndex+=1
      shipListIndex+=1
      for i in range(shipSize):
          battleshipPiecesTur.goto(currentX+65*i,currentY)
          battleshipPiecesTur.stamp()
          if player=="1":
              for j in range(len(player1BattleshipPiecesCoordinates)):
                  if [currentX+65*i,currentY] in player1BattleshipPiecesCoordinates or currentX+65*i>296:
                      needBreak=True
                      shipSizeListIndex-=1
                      shipListIndex-=1
                      battleshipPiecesTur.clearstamps()
                      battleshipPiecesTur.hideturtle()
                      print("battleship undo")
                      for k in range(amountToRemoveFromList):
                          player1BattleshipPiecesCoordinates.pop()
                      break
              if needBreak==True:
                  break
              else:
                  battleshipPiecesTur.showturtle()
              player1BattleshipPiecesCoordinates.append([currentX+65*i,currentY])
              amountToRemoveFromList+=1
          else:
              for j in range(len(player2BattleshipPiecesCoordinates)):
                  if [currentX+65*i,currentY] in player2BattleshipPiecesCoordinates or currentX+65*i>296:
                      needBreak=True
                      shipSizeListIndex-=1
                      shipListIndex-=1
                      battleshipPiecesTur.clearstamps()
                      battleshipPiecesTur.hideturtle()
                      print("battleship undo")
                      for k in range(amountToRemoveFromList):
                          player2BattleshipPiecesCoordinates.pop()
                      break
              if needBreak==True:
                  break
              else:
                  battleshipPiecesTur.showturtle()
              player2BattleshipPiecesCoordinates.append([currentX+65*i,currentY])
              amountToRemoveFromList+=1
      if shipListIndex>4:
          popUpScreen.destroy()
          shipListIndex=0
          shipSizeListIndex=0
          swapPlayer()
          wn.ontimer(clearScreenAndSetUpNextScreen,1000)
      else:
          infoLable.config(text=f"Player {player} type in the coordinate you what to place the {shipList[shipListIndex]} and the size is {shipSizeList[shipSizeListIndex]}.\nAfter you click the button then use the arrow keys to control the ship placement direction.")
      print(battleshipPiecesTurList)
  #function to place the ship to the left
  def placeShipToTheLeft():
      global row,currentX,currentY,shipListIndex,shipSizeList,shipSizeListIndex,infoLable,popUpScreen,player
      shipSize=shipSizeList[shipSizeListIndex]
      needBreak=False
      battleshipPiecesTur=t.Turtle("square",visible=False)
      battleshipPiecesTur.speed(0)
      battleshipPiecesTur.penup()
      battleshipPiecesTur.shapesize(3)
      battleshipPiecesTur.color("gray")
      amountToRemoveFromList=0
      shipSizeListIndex+=1
      shipListIndex+=1
      for i in range(shipSize):
          battleshipPiecesTur.goto(currentX-65*i,currentY)
          battleshipPiecesTur.stamp()
          if player=="1":
              for j in range(len(player1BattleshipPiecesCoordinates)):
                  if [currentX-65*i,currentY] in player1BattleshipPiecesCoordinates or currentX-65*i<-289:
                      needBreak=True
                      shipSizeListIndex-=1
                      shipListIndex-=1
                      battleshipPiecesTur.clearstamps()
                      battleshipPiecesTur.hideturtle()
                      for k in range(amountToRemoveFromList):
                          player1BattleshipPiecesCoordinates.pop()
                      break
              if needBreak==True:
                  break
              else:
                  battleshipPiecesTur.showturtle()
              player1BattleshipPiecesCoordinates.append([currentX-65*i,currentY])
              amountToRemoveFromList+=1
          else:
              for j in range(len(player2BattleshipPiecesCoordinates)):
                  if [currentX-65*i,currentY] in player2BattleshipPiecesCoordinates or currentX-65*i<-289:
                      needBreak=True
                      shipSizeListIndex-=1
                      shipListIndex-=1
                      battleshipPiecesTur.clearstamps()
                      battleshipPiecesTur.hideturtle()
                      for k in range(amountToRemoveFromList):
                          player2BattleshipPiecesCoordinates.pop()
                      break
              if needBreak==True:
                  break
              else:
                  battleshipPiecesTur.showturtle()
              player2BattleshipPiecesCoordinates.append([currentX-65*i,currentY])
              amountToRemoveFromList+=1
      if shipListIndex>4:
          popUpScreen.destroy()
          shipListIndex=0
          shipSizeListIndex=0
          swapPlayer()
          wn.ontimer(clearScreenAndSetUpNextScreen,1000)
      else:
          infoLable.config(text=f"Player {player} type in the coordinate you what to place the {shipList[shipListIndex]} and the size is {shipSizeList[shipSizeListIndex]}.\nAfter you click the button then use the arrow keys to control the ship placement direction.")
      print(battleshipPiecesTurList)
  #function to place the ship facing up
  def placeShipUp():
      global row,currentX,currentY,shipListIndex,shipSizeList,shipSizeListIndex,infoLable,popUpScreen,player
      shipSize=shipSizeList[shipSizeListIndex]
      needBreak=False
      battleshipPiecesTur=t.Turtle("square",visible=False)
      battleshipPiecesTur.speed(0)
      battleshipPiecesTur.penup()
      battleshipPiecesTur.shapesize(3)
      battleshipPiecesTur.color("gray")
      amountToRemoveFromList=0
      shipSizeListIndex+=1
      shipListIndex+=1
      for i in range(shipSize):
          battleshipPiecesTur.goto(currentX,currentY+65*i)
          battleshipPiecesTur.stamp()
          if player=="1":
              for j in range(len(player1BattleshipPiecesCoordinates)):
                  if [currentX,currentY+65*i] in player1BattleshipPiecesCoordinates or currentY+65*i>300:
                      needBreak=True
                      shipSizeListIndex-=1
                      shipListIndex-=1
                      battleshipPiecesTur.clearstamps()
                      battleshipPiecesTur.hideturtle()
                      for k in range(amountToRemoveFromList):
                          player1BattleshipPiecesCoordinates.pop()
                      break
              if needBreak==True:
                  break
              else:
                  battleshipPiecesTur.showturtle()
              player1BattleshipPiecesCoordinates.append([currentX,currentY+65*i])
              amountToRemoveFromList+=1
          else:
              for j in range(len(player2BattleshipPiecesCoordinates)):
                  if [currentX,currentY+65*i] in player2BattleshipPiecesCoordinates or currentY+65*i>300:
                      needBreak=True
                      shipSizeListIndex-=1
                      shipListIndex-=1
                      battleshipPiecesTur.clearstamps()
                      battleshipPiecesTur.hideturtle()
                      for k in range(amountToRemoveFromList):
                          player2BattleshipPiecesCoordinates.pop()
                      break
              if needBreak==True:
                  break
              else:
                  battleshipPiecesTur.showturtle()
              player2BattleshipPiecesCoordinates.append([currentX,currentY+65*i])
              amountToRemoveFromList+=1
      if shipListIndex>4:
          popUpScreen.destroy()
          shipListIndex=0
          shipSizeListIndex=0
          swapPlayer()
          wn.ontimer(clearScreenAndSetUpNextScreen,1000)
      else:
          infoLable.config(text=f"Player {player} type in the coordinate you what to place the {shipList[shipListIndex]} and the size is {shipSizeList[shipSizeListIndex]}.\nAfter you click the button then use the arrow keys to control the ship placement direction.")
      print(battleshipPiecesTurList)
  #function to place the ship facing down
  def placeShipDown():
      global row,currentX,currentY,shipListIndex,shipSizeList,shipSizeListIndex,infoLable,popUpScreen,player
      wn._bgcolor("black")
      shipSize=shipSizeList[shipSizeListIndex]
      needBreak=False
      battleshipPiecesTur=t.Turtle("square",visible=False)
      battleshipPiecesTur.speed(0)
      battleshipPiecesTur.penup()
      battleshipPiecesTur.shapesize(3)
      battleshipPiecesTur.color("gray")
      amountToRemoveFromList=0
      shipSizeListIndex+=1
      shipListIndex+=1
      for i in range(shipSize):
          battleshipPiecesTur.goto(currentX,currentY-65*i)
          battleshipPiecesTur.stamp()
          if player=="1":
              for j in range(len(player1BattleshipPiecesCoordinates)):
                  if [currentX,currentY-65*i] in player1BattleshipPiecesCoordinates or currentY-65*i<-285:
                      needBreak=True
                      shipSizeListIndex-=1
                      shipListIndex-=1
                      battleshipPiecesTur.clearstamps()
                      battleshipPiecesTur.hideturtle()
                      for k in range(amountToRemoveFromList):
                          player1BattleshipPiecesCoordinates.pop()
                      break
              if needBreak==True:
                  break
              else:
                  battleshipPiecesTur.showturtle()
              player1BattleshipPiecesCoordinates.append([currentX,currentY-65*i])
              amountToRemoveFromList+=1
          else:
              for j in range(len(player2BattleshipPiecesCoordinates)):
                  if [currentX,currentY-65*i] in player2BattleshipPiecesCoordinates or currentY-65*i<-285:
                      needBreak=True
                      shipSizeListIndex-=1
                      shipListIndex-=1
                      battleshipPiecesTur.clearstamps()
                      battleshipPiecesTur.hideturtle()
                      for k in range(amountToRemoveFromList):
                          player2BattleshipPiecesCoordinates.pop()
                      break
              if needBreak==True:
                  break
              else:
                  battleshipPiecesTur.showturtle()
              player2BattleshipPiecesCoordinates.append([currentX,currentY-65*i])
              amountToRemoveFromList+=1
      if shipListIndex>4:
          popUpScreen.destroy()
          shipListIndex=0
          shipSizeListIndex=0
          swapPlayer()
          wn.ontimer(clearScreenAndSetUpNextScreen,1000)
      else:
          infoLable.config(text=f"Player {player} type in the coordinate you what to place the {shipList[shipListIndex]} and the size is {shipSizeList[shipSizeListIndex]}.\nAfter you click the button then use the arrow keys to control the ship placement direction.")
  #Function that creates the board
  def makeBoard():
      global hasBothPlayerPlaceThereShipsDown,player
      wn.setup(height=700)
      wn.title("Battleship")
      wn.bgcolor("black")
      theNumberToAddToIntergoal=0
      numberThatNeedToAddToX=0
      numberThatNeedToAddToY=0
      asciiValue=65
      number=1
      for i in range(100):
          gameBoard=t.Turtle(shape="square",visible=False)
          gameBoard.speed(0)
          gameBoard._tracer(3)
          gameBoard.penup()
          gameBoard.shapesize(3)
          if i==10+theNumberToAddToIntergoal:
              asciiValue+=1
              numberThatNeedToAddToY+=65
              theNumberToAddToIntergoal+=10
              numberThatNeedToAddToX=0
              letterLableWriter.goto(-335,290-numberThatNeedToAddToY)
          else:
              numberThatNeedToAddToX+=65
              numberLableWiter.goto(-295+numberThatNeedToAddToX,327)
              if i==0:
                  numberThatNeedToAddToX=0
                  letterLableWriter.goto(-335,290)
                  numberLableWiter.goto(-295,327)
          gameBoard.goto(-289+numberThatNeedToAddToX,300-numberThatNeedToAddToY)
          letterLableWriter.write(chr(asciiValue),font=fontSetting)
          if hasBothPlayerPlaceThereShipsDown==True:
              if player=="1":
                  if [-289+numberThatNeedToAddToX,300-numberThatNeedToAddToY] in player1HitCoordinatesList:
                      gameBoard.color("red")
                  elif [-289+numberThatNeedToAddToX,300-numberThatNeedToAddToY] in player1MissCoordinatesList:
                      gameBoard.color("white")
                  else:
                      gameBoard.color("skyblue")
              else:
                  if [-289+numberThatNeedToAddToX,300-numberThatNeedToAddToY] in player2HitCoordinatesList:
                      gameBoard.color("red")
                  elif [-289+numberThatNeedToAddToX,300-numberThatNeedToAddToY] in player2MissCoordinatesList:
                      gameBoard.color("white")
                  else:
                      gameBoard.color("skyblue")
          else:
              gameBoard.color("skyblue")
          if number<=10:
              numberLableWiter.write(number,font=fontSetting)
          number+=1
          gameBoard.showturtle()
          gameBoard._tracer(0)
      popUpMenu()
  #function to clear the screen and make a new one
  def clearScreenAndSetUpNextScreen():
      wn.clear()
      makeBoard()
  #function to swap the players  
  def swapPlayer():
      global player,player1BattleshipPiecesCoordinates,player2BattleshipPiecesCoordinates,hasBothPlayerPlaceThereShipsDown
      if player=="1":
          player="2"
      else:
          player="1"
      if len(player1BattleshipPiecesCoordinates)!=0 and len(player2BattleshipPiecesCoordinates)!=0:
          hasBothPlayerPlaceThereShipsDown=True
  #function to detect hits
  def hitDetection():
      global currentX,currentY,player1BattleshipPiecesCoordinates,player2BattleshipPiecesCoordinates
      print("In the hitDetection")
      print(player1BattleshipPiecesCoordinates)
      print()
      print(player2BattleshipPiecesCoordinates)
      hasAPlayerWin=False
      hitCounter=0
      hitOrMissTurtles=t.Turtle("square",visible=False)
      hitOrMissTurtles.speed(0)
      hitOrMissTurtles.penup()
      hitOrMissTurtles.shapesize(3)
      hitOrMissTurtles.goto(currentX,currentY)
      destroyShipWriter=t.Turtle(visible=False)
      destroyShipWriter.speed(0)
      destroyShipWriter.penup()
      destroyShipWriter.color("green")
      if player=="1":
          print("player=",player)
          #checks to see if the current input is a hit or a miss
          if [currentX,currentY] in player2BattleshipPiecesCoordinates:
              hitOrMissTurtles.color("red")
              hitOrMissTurtles.stamp()
              print("It is a hit")
              player1HitCoordinatesList.append([currentX,currentY])
              for i in range(len(player2BattleshipPiecesCoordinates)):
                  if player2BattleshipPiecesCoordinates[i] in player1HitCoordinatesList:
                      hitCounter+=1
                  else:
                      hitCounter=0
                  if hitCounter==5 and i==4:
                      if "carrier" in player2ShipList:
                          player2ShipList.remove("carrier")
                          print("ship destroyed")
                          destroyShipWriter.write("Ship Destroyed",font=fontSetting)
                      hitCounter=0
                  elif hitCounter==4 and i==8:
                      if "battleship" in player2ShipList:
                          player2ShipList.remove("battleship")
                          destroyShipWriter.write("Ship Destroyed",font=fontSetting)
                      hitCounter=0
                  elif hitCounter==3 and i==11:
                      if "cruiser" in player2ShipList:
                          player2ShipList.remove("cruiser")
                          destroyShipWriter.write("Ship Destroyed",font=fontSetting)
                      hitCounter=0
                  elif hitCounter==3 and i==14:
                      if "submarine" in player2ShipList:
                          player2ShipList.remove("submarine")
                          destroyShipWriter.write("Ship Destroyed",font=fontSetting)
                      hitCounter=0
                  elif hitCounter==2 and i==16:
                      if "destroyer" in player2ShipList:
                          player2ShipList.remove("destroyer")
                          destroyShipWriter.write("Ship Destroyed",font=fontSetting)
                      hitCounter=0
                  if len(player2ShipList)==0:
                      hasAPlayerWin=True
                      print("player 1 wins")
          else:
              hitOrMissTurtles.color("white")
              print("It is a miss")
              hitOrMissTurtles.stamp()
              player1MissCoordinatesList.append([currentX,currentY])
      else:
          if [currentX,currentY] in player1BattleshipPiecesCoordinates:
              hitOrMissTurtles.color("red")
              hitOrMissTurtles.stamp()
              player2HitCoordinatesList.append([currentX,currentY])
              print("It is a hit")
              for i in range(len(player1BattleshipPiecesCoordinates)):
                  if player1BattleshipPiecesCoordinates[i] in player2HitCoordinatesList:
                      hitCounter+=1
                  else:
                      hitCounter=0
                  if hitCounter==5 and i==4:
                      if "carrier" in player1ShipList:
                          player1ShipList.remove("carrier")
                          print("ship destroyed")
                          destroyShipWriter.write("Ship Destroyed",font=fontSetting)
                      hitCounter=0
                  elif hitCounter==4 and i==8:
                      if "battleship" in player1ShipList:
                          player1ShipList.remove("battleship")
                          destroyShipWriter.write("Ship Destroyed",font=fontSetting)
                      hitCounter=0
                  elif hitCounter==3 and i==11:
                      if "cruiser" in player1ShipList:
                          player1ShipList.remove("cruiser")
                          destroyShipWriter.write("Ship Destroyed",font=fontSetting)
                      hitCounter=0
                  elif hitCounter==3 and i==14:
                      if "submarine" in player1ShipList:
                          player1ShipList.remove("submarine")
                          destroyShipWriter.write("Ship Destroyed",font=fontSetting)
                      hitCounter=0
                  elif hitCounter==2 and i==16:
                      if "destroyer" in player1ShipList:
                          player1ShipList.remove("destroyer")
                          destroyShipWriter.write("Ship Destroyed",font=fontSetting)
                      hitCounter=0
                  if len(player1ShipList)==0:
                      hasAPlayerWin=True
                      print("player 2 wins")
          else:
              hitOrMissTurtles.color("white")
              print("It is a miss")
              hitOrMissTurtles.stamp()
              player2MissCoordinatesList.append([currentX,currentY])
      hitOrMissTurtles.showturtle()
      popUpScreen.destroy()
      if hasAPlayerWin==True:
          wn.clear()
          winWriterTurtle=t.Turtle()
          winWriterTurtle.color("skyblue")
          winWriterTurtle.write(f"player {player} wins",font=winFontSetting)
      else:
          swapPlayer()
          wn.ontimer(clearScreenAndSetUpNextScreen,1000)
  makeBoard()
  board.mainloop()
#end of Kapp portion

def creditMaker():
  #creates the screen for the credits
  creditScreen=t.Screen()
  creditScreen.setup(height=500,width=500)

  #writes the credits
  creditWriter=t.Turtle(visible=False)
  creditWriter.penup()
  creditWriter.goto(-200,0)
  creditWriter.write(credits,font=("Arial",11,"bold","underline"))

  #creates the back button
  backTurtle=t.Turtle(visible=False)
  backTurtle.penup()
  backTurtle.setposition(-150,210)
  backTurtle.write("EXIT-press e to leave",align="center",font=("Arial",11,"bold"))

  #the function to leave the directions and return to the main menu
  def leaveCredits():
    creditScreen.clearscreen()
    menu()

  #the onkeypress to call leaveDirection
  creditScreen.onkeypress(leaveCredits,"e")  

  creditScreen.mainloop()

#opens the main menu
menu()

#opens the menus when you press the number keys
wn.onkeypress(openPvP,"1")
wn.onkeypress(mainScreenClear,"2")
wn.onkeypress(openCredits,"3")
wn.listen()

wn.mainloop()
#end of Camp Portion