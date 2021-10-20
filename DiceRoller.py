import random
import sys

def diceRoll(n: int) -> int:
  '''
  You can make this general to be for any n or you could do the 
  check of n here
  '''
  dice = random.randint(1,n)  
  print("Your number is " + str(dice) + "!\n")

def roll() ->None:
  '''
  A method to begin rolling the die.
  Continue to ask the two main quesions and roll the die until
  the user hits esc. 
  '''
  while True:  
    die_num = input("What are the number of sides on the die? (2/4/6/10/20): ")
    
    if die_num not in ['2', '4', '6', '10', '20']:
      print('Invalid number')
      break

    question = input("Roll the dice? y/n: ")
    
    if question == "n":
      print("Aborting...")
      sys.exit()
    else:
      diceRoll(int(die_num))

if __name__ == "__main__":
  roll()


  
   
