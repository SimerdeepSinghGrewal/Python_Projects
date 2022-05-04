from art import *
from game_data import data
import random
import os


value4=0
score=0
def select_random():
  item= random.choice(data)
  value1= item['name']
  value2= item['description']
  value3= item['country']
  global value4
  value4= item['follower_count']
  return (f"{value1} , a {value2}, from {value3}")
  
again= False
re_run= True

clear = lambda: os.system('cls')
clear()
print(logo)
person1= select_random()
print(f"Compare A: {person1}")
follow1= value4
print(value4)
while re_run:
  if again:
    
    print(f"Compare A: {person2}")
    follow1= follow2
    print(follow2)
  print(vs)
  person2= select_random()
  print(f"Against B: {person2}")
  print(value4)
  follow2= value4 
  choice= input("Who has more followers? Type 'A' or 'B' : ")
  if choice == "a" or choice == "A":
    if follow1 > follow2:
      clear()
      print(logo)
      score += 1
      print(f"You're right. Current score {score}.")
      again= True
    else:
      clear()
      print(f"Sorry, That's wrong. Final score {score}.")
      re_run= False
  elif choice == "b" or choice == "B":
    if follow1 < follow2:
      clear()
      print(logo)
      score += 1
      print(f"You're right. Current score {score}.")
      again= True
    else:
      clear()
      print(f"Sorry, That's wrong. Final score {score}.")
      re_run= False
  else:
    print("Enter a valid option. ")
  
