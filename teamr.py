from random import *
from time import *

roomArray = []
itemArray = []


for i in range(999):
    roomArray.append(False)
    itemArray.append(False)


roomNumbers = [0, 1, 2, 3, 100, 200, 101, 201, 103, 104, 105, 203, 204, 302, 303, 402, 403]

choices = ["n", "e", "s", "w"]
location = 0
inventory = []



def doesRoomExist(roomNumber):
    try:
          if roomArray[roomNumber] is False:
            
            print("You can't go there")
            return False

          else:
            return True
    except IndexError:
        
        print("You can't go there")
        return False

    

roomArray[0] = "You find yourself in the basement of house on a chair. There is a loose nail in the chair. There are walls to the North and West of you. To the East there is a rug, and to the South there are stairs." 
roomArray[1] = "To the South is the stairs. To the east there is something in a frame, but you don't know what it is."
roomArray[2]= "You are at the bottom of the stairs. The chair is south of you and you see some paintings on the wall. "
roomArray[3] = "You are at the top of the stairs. To the east you see a pile of old books. To the north there are stairs. There are walls west and south of you. "
roomArray[100] = "You are standing on a very damp rug. There is a weird bump on the rug, it looks suspicious."
roomArray[200] = "To the north and east there is a wall. To the south you see a something in a frame."
roomArray[101] = "To the north of you there is a moist rug. To the east of you there is something that looks like a paper in a picture frame."
roomArray[201] = "There is a wall to the east and south of you. In the corner you see a high school diploma in the picture frame."
roomArray[302] = "There is a wall to the North and West of you. In reach you see a Spatuala tha looks useful. To the east of you you see soemthing that looks like food"
roomArray[402] = "There is a wall to the North and East of you. You see some tasty Cheetos in view. In the South you see soemthing that looks locked"
roomArray[403] = "Congragulations, you escaped!!!"
roomArray[303] = "To the south you see a wall. On the counter you see Sink with the tap still on. To the east of you there looks like some sort of window in reach, but it looks like you need something to open it."
roomArray[103] = "The stairs lie to the west and a bright light hangs overhead. A pile of books are on the floor, askew."
roomArray[203] = "The light to the west illuminates the area and reveals the spatula in the kitchen, to the east."
roomArray[104] = "The book pile sits to the north and a tall stack of pillows are shown to the east. There is a bathroom with the door shut to the south."
roomArray[204] = "The pillows surround you, creating a fluffy padding on the floor. Another light shines to the north, revealing an enterance to another room."
roomArray[105] = "You are in the bathroom. There is a old toilet and it smells like vinegar."

itemArray[0] = "Nail"
itemArray[100] = "Watch"
itemArray[201] = "Diploma"
itemArray[302] = "Spatula"
itemArray[402] = "Cheetos"
itemArray[103] = "Books"
itemArray[204] = "Pillows"




def move(userInput, location):


  if userInput == "n" and doesRoomExist(location-1) == True:
      location -= 1
  if userInput == "e" and doesRoomExist(location+100) == True:
      location += 100
  if userInput == "s" and doesRoomExist(location+1) == True:
      location += 1
  if userInput == "w" and doesRoomExist(location-100) == True:
      location -= 100
  return location
def items(location):
    if location == 402 and "Cheetos" not in inventory:
      print("You have cheetos, snonk!")
      inventory.append("Cheetos")
    if location == 0 and "Nail" not in inventory:
      print("You picked up a rusty nail!")
      inventory.append("Nail")
      
    if location == 100 and "Watch" not in inventory:
      print("You gained a very valuable watch!")
      inventory.append("Watch")
    if location == 201 and "Diploma" not in inventory:
      print("You now have a high school diploma!")
      inventory.append("Diploma")
    if location == 302 and "Spatula" not in inventory:
        print("You have snonched a Spatula!")
        inventory.append("Spatula")
    if location == 303:
        print("You've turned off the water for the sink")
    if location == 103 and "Books" not in inventory:
        print("You have stolen books, start reading!")
        inventory.append("Books")
    if location == 204 and "Pillows" not in inventory:
        print("You have damp pillows, sleep after you escape!")
        inventory.append("Pillows")
    if location == 105 and "Key" not in inventory:
        print("You found a key")
        inventory.append("Key")

def main():
  location = 0
  print("The Escape")
  print("By Dhruv, Taylor, Rishil, and Buk")
  sleep(1)
  
  while True:

    print(roomArray[location])
    items(location)
    print("Please type n, s, e, w, or quit")
    userInput = input()
    userInput = userInput.lower()
    if userInput in choices:
      location = move(userInput, location)

    if userInput == "quit": 
        break
    if location == 403:
        print(roomArray[location])
        break



     






