import random
'''
1 for snake
-1 for water 
0 for gun
'''
def playgame ():
    computer = random.choice([-1, 0, 1])        # a module so computer choose random no .
    youstr = input("Enter your choice: ")       #youstr is variable which take our input in string as s, w or g
    youDict = {"s": 1, "w": -1, "g": 0}         #youdict then assign value pairs to the inputs likr 1,-1,0 and store them in a dictionary
    reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}  
# youDict: Maps the user input (s, w, g) to corresponding numerical values.
# reverseDict: Maps numerical values back to the names of the choices for display purposes.
    you = youDict[youstr]
# The user's input string is converted into its corresponding numerical value.

# By now we have 2 numbers (variables), you and computer

    print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")  # displaying choices
#reverse dict to show user back in the form he inputted, so 1:snake, will show user u choose snake 

    if(computer == you):
        print("Its a draw")

    else:
        if(computer ==-1 and you == 1): 
            print("You win!")

        elif(computer ==-1 and you == 0):
            print("You Lose!")

        elif(computer == 1 and you == -1):
            print("You lose!")

        elif(computer ==1 and you == 0):
            print("You Win!")

        elif(computer ==0 and you == -1):
            print("You Win!")

        elif(computer == 0 and you == 1):
            print("You Lose!")

        else:
            print("Something went wrong!")



while True:
    playgame()
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break        