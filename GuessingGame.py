#GuessingGame.py
#Zeke Amonoo
#This program generates a vast majority of numbers for a game

import random

guessesTaken = 0
count = 0


print("Welcome to the guessing game!")
print("I’ll pick a number from 1 to 9 and you’ll have 5 chances to guess it")
while (count <= 5):
    (int(input("Enter your guess: "))

digit=random.randint(1,9)
     
while guessesTaken < 6:

    guessesTaken = guessesTaken + 1

    if guess < digit:
       print("Your guess is too low.") 

    if guess > digit:
       print("Your guess is too high.")

    if guess == digit:
       break

if guess == digit:
    guessesTaken = str(guessesTaken)
    print("You guessed" + guessesTaken + "That’s amazing!")

if guess != digit:
    number = str(digit)
    print("Sorry, the random number was" + digit ".Better luck next time.")
