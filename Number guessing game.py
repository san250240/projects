# This is a number guessing game.

import random

print ("What is your name?")
name = input()
print ("Well " + name + ", I'm thinking of a number between 1 and 10. Take a guess.")
secretnum = random.randint(1, 10)

for guessestaken in range(1, 7):
    try:
        print ("Take a guess!")
        guess = input()
        if int(guess) > secretnum:
            print ("Your number is too high.")
        elif int(guess) < secretnum:
            print ("Your number is too low.")
        else:
            break
    except:
        print ("Please enter a number.")

if int(guessestaken) == 1:
    print ("Congratulations, you guessed it right in 1 try.")
elif int(guessestaken) == secretnum and int(guess) != 1:
    print ("Congratulations, you guessed it right in " + str(guessestaken) + " tries.")
else:
    print ("Nope, I was thinking " + str(secretnum) + ".")