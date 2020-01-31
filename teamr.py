from random import *
from time import *
roomNumbers = [0,1,2,3,100,200,101,201,103,104,105,203,204,302,303.402,403]
roomArray = [] 
itemArray = ["chair", "damp rug", "diploma", "books", "pillows", "key", "spatula", "cheeto"]
itemCoords = {}
itemCoords["books"] = 103
itemCoords["pillows"] = 204

for i in range(999):
    roomArray.append(False)

roomArray[0] = "You find yourself in the basement of house on a chair. There is a loose nail in the chair. There are walls to the North and West of you. To the East there is a rug, and to the South there are stairs." 
roomArray[1] = "To the South is the stairs. To the east there is something in a frame, but you don't know what it is."
roomArray[100] = "You are standing on a very damp rug. There is a weird bump on the rug, it looks suspicious."
roomArray[200] = "To the north and east there is a wall. To the south you see a something in a frame."
roomArray[101] = "To the north of you there is a moist rug. To the east of you there is something that looks like a paper in a picture frame."
roomArray[201] = "There is a wall to the east and south of you. In the corner you see a high school diploma in the picture frame."
roomArray[103] = "The stairs lie to the west and a bright light hangs overhead. A pile of books are on the floor, askew."
roomArray[203] = "The light to the west illuminates the area and reveals the spatula in the kitchen, to the east."
roomArray[104] = "The book pile sits to the north and a tall stack of pillows are shown to the east."
roomArray[204] = "The pillows surround you, creating a fluffy padding on the floor. Another light shines to the north, revealing an enterance to another room."

def doesRoomExist(roomNumber):
    try:
        if roomArray[roomNumber] == False:
            print("You can't go there!")
            return False
        else:
            return True
    except:
        print("You can't go there!")
        return False

def move(userInput, location):
    userInput = userInput.lower()
    if userInput == "n" and roomDoesExist(location - 1):
        location -= 1
    if userInput == "e" and roomDoesExist(location - 1):
        location += 100
    if userInput == "s" and roomDoesExist(location - 1):
        location += 1
    if userInput == "w" and roomDoesExist(location - 1):
        location -= 100
    else:
        print("Invalid option!")


if location == 402:
    print("You have cheetos, good job")
    inventory.append("Cheetos")
if location == 0:
    print("You have a Nail in your inventory.")
    inventory.append("Nail")
if location == 100:
    print("You have a very valuable watch.")
    inventory.append("Watch")
if location == 201:
    print("You now have a high school diploma.")
    inventory.append("Diploma")

def main():
  location = 0
  print("The Escape")
  print("By Dhruv, Taylor, Rishil, and Buk")
  sleep(1)
  while True:
    print("")
    print("Please type n, s, e, w, or quit")
    userInput = input()
    move(userInput,location)
    location = userInput()

