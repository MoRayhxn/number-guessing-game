### refined version of previous number guessing game i made
import random
### allows computer and player to choose a number
x = random.randint(1,100)
guess = int(input("What is X? "))
### as long as we dont choose the wrong number, it will tell us if we need to guess lower or higher and prompt us to guess again
while guess != x:
    print("Lower") if guess > x else print("Higher")
    guess = int(input("What is X"))
### if guess is == it will leave the while loop and tell us we was correct
print("Correct!")