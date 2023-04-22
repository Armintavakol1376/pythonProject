# first I need produce random number.
import random

num = random.randint(1, 100)
guess = None
tries = 0

print(" whats your guess number?")

while guess != num:
    guess = int(input("inter your guess :"))
    tries += 1

    if num > guess:
        print("its too short")

    elif num < guess:
        print("its too high")

    else:
        print(("Congratulations, you guessed it in", tries, "tries!"))


