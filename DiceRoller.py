import random
import sys


def diceRoll(n: int) -> int:
        dice = random.randint(1,n)  
        print("Your number is " + str(dice) + "!")
        return dice


while 1:  
  die_num = input("What are the number of sides on the die? (2/4/6/10/20): ")
  question = input("Roll the dice? y/n: ")
  
  if die_num not in ['2', '4', '6', '10', '20']:
    break

    if die_num == "2":
      print(question)
    if question == "y":
      diceRoll2()
  if question == "n":
    print("Aborting...")
    sys.exit()

  if die_num == "4":
    print(question)
    if question == "y":
      diceRoll4()
  if question == "n":
    print("Aborting...")
    sys.exit()

  if die_num == "6":
    print(question)
    if question == "y":
      diceRoll6()
  if question == "n":
    print("Aborting...")
    sys.exit()

  if die_num == "10":
    if question == "y":
      diceRoll10()
  if question == "n":
    print("Aborting...")
    sys.exit()
    
  if die_num == "20":
    print(question)
  if question == "y":
      diceRoll20()
  if question == "n":
    print("Aborting...")
    sys.exit()
  
  

  
   
