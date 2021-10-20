import random
import sys


def diceRoll2():
        dice2 = random.randint(1,2)  
        print("Your number is " + str(dice2) + "!")
def diceRoll4():
        dice4 = random.randint(1,4)  
        print("Your number is " + str(dice4) + "!")
def diceRoll6():
        dice6 = random.randint(1,6)  
        print("Your number is " + str(dice6) + "!")
def diceRoll10():
        dice10 = random.randint(1,10)  
        print("Your number is " + str(dice10) + "!")
def diceRoll20():
        dice20 = random.randint(1,20)  
        print("Your number is " + str(dice20) + "!")

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
  
  

  
   
