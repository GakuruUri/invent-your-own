" This is a guess the number game"
import random

guessTaken = 0

print("Hello! what is your name?")
myName = input()

number = random.randint(1, 20)
print(f"Well,{myName}, I am thinking of a number between 1 and 20.")

for guessTaken in range(6):
    print("Take a guess.")
    guess = input()
    guess = int(guess)

    if guess < number:
        print("your guess is too low.")

    if guess > number:
        print("Your guess is too high")

    if guess == number:
        break

if guess == number:
    guessTaken = str(guessTaken + 1)
    print(f"Good job, {myName}! You guessed my number in {guessTaken} guesses!")

if guess != number:
    number = str(number)
    print("Nope. The number I was thinking of was '+ number + '.")








