#!/usr/bin/env python

import random

def main():
  """Start a music genre  guessing game."""
  print("Guess the music genre!") 
 
musicgenre = [
          "pop" ,
          "hip-hop" ,
          "jazz" ,
          "slowed" ,
          "remix" ,
          "rock" ,
          "dangdut" ,
          "heavy metal" ,
          ]
  
x = random.choice(musicgenre)

print("\nHi everyone.Let's play the quessing game")
print("\n**************************************")
print("\nYour game start in 5 second")
 
guess = None

import time 

print("Ready to answer the questions?")
time.sleep(5)
print("Your game start now GOODLUCK")


for count in range(3):

    guess = str(input("\nWhat kind of music genre that i like: "))

    if x == guess:
        print("You guessed {}. Correct!,you're genius".format(guess))
        break
    else:
        print("You guessed {}. Ups!,you've got it wrong.".format(guess))                           
else:
    print("\nTimes up!")          
    print("\nThe correct answer is :" , x )
    
    
