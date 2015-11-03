import random

guess = 0
guesses = 3
number = random.randint(1,10)

name = input("What is your name?\n    ")
print("Let's play a game " + name + ". I am thinking of a number from 1 to 10.\n Which number is it? You have 3 tries")

while guesses != 0:
    guess = input("Guess a number from 1-10.\n    ")
 
    guess = int(guess)

    guesses = guesses - 1

    if guess > number:
        print("Your guess is too high. ")

    if guess < number:
        print("Your guess is too low. ")

    if guess == number:
        break

if guess == number:
    print("You guessed it right " + name + "! " + " Those were 3 in 10 odds!")

if guess != number:
    print("Better luck next time " + name + ". Thanks for playing.")
