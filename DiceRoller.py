import random
import sys

def diceRoll(n: int) -> int:
        dice = random.randint(1,n)  
        print("Your number is " + str(dice) + "!")

while True:  
  die_num = input("What are the number of sides on the die? (2/4/6/10/20): ")
  
  if die_num not in ['2', '4', '6', '10', '20']:
    break

  question = input("Roll the dice? y/n: ")
  
  if question == "n":
    print("Aborting...")
    sys.exit()
  else:
    diceRoll(int(die_num))


  
   
