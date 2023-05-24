######HIGHER-LOWER GAME######

#IMPORTS#
from game_data import data
from art import logo, vs
from random import randint
from replit import clear

#Set score
score = 0

#Generate a random numbers
nr1 = randint(0, 49)
A = data[nr1]

def game():
  global A
  global score
  print(logo, '\n')
  #Start of game loop
  game_over = False
  
  while not game_over:
    nr2 = randint(0, 49)
    B = data[nr2]
    if A == B:
      B = data[randint(0,49)]

    #Initial screen
    
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
    
    print('\n', vs, '\n')
    
    print(f"B: {B['name']}, a {B['description']}, from {B['country']}.")
    
    #Ask which is higher
    follow_a = A['follower_count']
    follow_b = B['follower_count']
    
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    
    if follow_a > follow_b and answer == 'a':
      score += 1
      A = B
      clear()
      print(logo, '\n')
      print(f"You're right! Current score: {score}")
      #game()
    elif follow_a > follow_b and answer == 'b':
      print(f"Sorry, that's wrong. Final score: {score}")
      game_over = True
    elif follow_a < follow_b and answer == 'b':
      score += 1
      A = B
      clear()
      print(logo, '\n')
      print(f"You're right! Current score: {score}")
      #game()
    else:
      print(f"Sorry, that's wrong. Final score: {score}")
      game_over = True

game()