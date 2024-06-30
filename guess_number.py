# This is as guess the number game
import random

guessTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1, 20)
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.')

for guessTaken in range(6):
    print('Take a guess')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Your guess is too low.')

    elif guess > number:
        print('Your guess is too high.')

    else:
        break

if guess == number:
    guessTaken = str(guessTaken + 1 )
    print('Good Job, ' + myName + '! You guessed my number in ' + guessTaken + ' guesses!')
if guess != number:
    number = str(number)