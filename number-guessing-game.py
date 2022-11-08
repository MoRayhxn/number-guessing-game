import random

### Allows program to choose a number
number = random.randint(1, 50)

### Allows user to guess
guess = int(input("Enter Guess between 1-50: "))


### If guess is not equal to the number it will check if the guess is too low, if so it will prompt user to guess higher. If not, it will prompt user to guess lower and print that you got it correct when you do.
while guess != number:  
    if guess < number:
        print("Maybe try a little higher")
        guess = int(input("\nEnter Guess between 1-50: "))
    else:
        print("Maybe try a little lower")
        guess = int(input("\nEnter Guess between 1-50: "))

print("Congratulations, you got it right!")

        


