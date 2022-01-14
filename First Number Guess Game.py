
from colorama import Fore, Back, Style
import random
import time



        
easy = random.randint(1, 10)
medium = random.randint(1, 100)
hard = random.randint(1, 1000)

easyanswer = str(easy)
mediumanswer = str(medium)
hardanswer = str(hard)

print(Fore.MAGENTA + ("Welcome to My first random number guessing game"))

cheat = input(Fore.MAGENTA + ("Would you like to see the results before continuing? y/n ")) 


print(Fore.BLUE + ("What difficulty would you like to play? "))

print(Fore.GREEN + ("For Easy (1-10) type 1"))
print(Fore.YELLOW + ("For Medium (1-100) type 2"))
print(Fore.RED + ("For Hard (1-1000) type 3"))
print(Fore.WHITE)
if cheat  == ("y"):
  Fore.WHITE
  print("Easy answer " + easyanswer, "Medium answer " + mediumanswer, "Hard answer " + hardanswer)
dif = input(Fore.WHITE)

if dif == ("1"):
  print(Fore.GREEN + ("You have chosen Easy!"))
  time.sleep(1)
  guess = input(Fore.GREEN + ("Please select a random number between 1 and 10: "))
  print(Fore.GREEN + ("The number you chose was " + guess))
  if guess == (easyanswer):
    print(Fore.GREEN + ("The correct answer was " + guess + " congrats you win!"))
  if guess != (easyanswer):
    print(Fore.GREEN + ("The correct answer was " + easyanswer + " sorry you lose"))
    
if dif == ("2"):
  print(Fore.YELLOW + ("You have chosen Medium!"))
  time.sleep(1)
  guess = input(Fore.YELLOW + ("Please select a random number between 1 and 100: "))
  print(Fore.YELLOW + ("The number you chose was " + guess))
  if guess == (mediumanswer):
    print(Fore.YELLOW + ("The correct answer was " + guess + " congrats you win!"))
  if guess != (mediumanswer):
    print(Fore.YELLOW + ("The correct answer was " + mediumanswer + " sorry you lose"))
    
if dif == ("3"):
  print(Fore.RED + ("You have chosen Hard!"))
  time.sleep(1)
  guess = input(Fore.RED + ("Please select a random number between 1 and 1000: "))
  print(Fore.RED + ("The number you chose was " + guess))
  if guess == (hardanswer):
    print(Fore.RED + ("The correct answer was " + guess + " congrats you win!"))
  if guess != (hardanswer):
    print(Fore.RED + ("The correct answer was " + hardanswer + " sorry you lose"))
  

  






  
  
  