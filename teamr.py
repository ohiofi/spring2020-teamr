
import time
def main():
  location = 0
  print("The Escape")
  print("By Dhruv, Taylor, Rishil, and Buk")
  time.sleep(1)
  while True:
    print("")
    print("Please type n, s, e, w, or quit")
    userInput = input()
    move(userInput,location)
    location = userInput()
   
