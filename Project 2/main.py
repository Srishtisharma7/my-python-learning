'''We are going to write a program that generates a random number and asks the user to
guess it.
If the player's guess is higher than the actual number, the program displays “Lower
number please”. Similarly, if the user's guess is too low, the program prints “higher
number please” When the user guesses the correct number, the program displays the
number of guesses the player used to arrive at the number.'''

import random
n = random.randint(1, 100) 
a = -1    # Sets the initial guess to -1 (a value guaranteed not to match the random number n). as ranint range between 1 to 100
guesses = 1

while(a != n):         # the loop runs until the user guesses the correct number (a == n).
    a = int(input("Guess the number: ")) 
    if(a >n):
        print("Lower number please")
        guesses +=1
    elif(a<n):
        print("Higher number Please")
        guesses +=1

print(f"You have guessed the number {n} correctly in {guesses} attempts")