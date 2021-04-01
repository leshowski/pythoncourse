import random
import time
number = random.randint(1,10)
guess = 0
tries = 0

name = input("Hello, may I know your Name:?")
print("Hello "+name+".")

question = input("Are you Ready to Guess? [Y/N]:")
time.sleep(1)

if question.lower() != 'y':
    time.sleep(1)
    print("I'm sorry, We'll meet each other next time!")
    exit()
if question.lower() == 'y':
    time.sleep(1)
    print("I'm thinking of a number between 1 & 10")

while not (guess == number):
    time.sleep(1)
    guess = int(input("What's your Guess?:"))
    tries = tries +1
    if(guess == number):
        print("Brilliant")
        time.sleep(1)
        print("Congrats, Your Guess was correct")
        print(f"The number was indeed {format(number)}")
        print(f"It has taken you {tries} times")
    elif guess < number:
        print("No! Guess Higher")
    else:
        print("No! Guess Lower")
        