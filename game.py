# use the needed libraries
import random
from cs50 import get_int

# use the while loop for get the user positive value
while True:
    level = get_int("Level: ")
    if level > 0:
        break
# get the random value using random libarary randint function
value = random.randint(1, level)

# set the guess value 0
guess = 0

# use the while for user guess right values just right
while guess != value:
    guess = get_int("Guess: ")
    if guess == value:
        print("Just right!")
        break
    elif guess > value:
        print("Too large!")
    else:
        print("Too small")