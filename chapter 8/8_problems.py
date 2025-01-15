# 1. Write a program to read the text from a given file ‘poems.txt’ and find out  whether it contains the word ‘twinkle’.

f = open("/Users/srishtisharma/python/code harry/chapter 8/poem.txt")
content = f.read()
if("twinkle" in content):
    print("The word twinkle is present in the content")

else:
    print("The word twinkle is not present in the content")

f.close()





# 2. The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
# contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score.

import random

def game(): 
    print("You are playing the game..")
    score = random.randint(1, 62)     
    #game function generates the random score using random.randit and prints the message
    # Fetch the hiscore

    with open("/Users/srishtisharma/python/code harry/chapter 8/hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore!=""):       #until it ends
            hiscore = int(hiscore)          #if data , then read and convert it into int
        else:
            hiscore = 0   #if blank set hiscore = 0

#Reading the Hi-score:
# Opens the file hiscore.txt in read mode to fetch the previous Hi-score.
# If the file contains data, it reads and converts it into an integer (hiscore).
# If the file is blank, it sets hiscore to 0 by default.
#     print(f"Your score: {score}")

        print(f"Your score: {score}")
    if(score>hiscore):
        # write this hiscore to the file
        with open("/Users/srishtisharma/python/code harry/chapter 8/hiscore.txt", "w") as f:
            f.write(str(score))    #string input

    return score      #Returns the player's score.

game()

#compare the current game score (score) with the fetched Hi-score (hiscore).
#if the current score exceeds the Hi-score, it opens the file hiscore.txt in write mode and
# writes the new Hi-score (which is string inputted score from the user and it replaces the random generated hiscore which was set to 0
# since user input is greater than random score ) into the file.



# Initially, the file hiscore.txt is empty.
# The player plays the game and gets a score of 45. Since there's no previous Hi-score, 45 is written to the file.
# The player plays again and scores 30. The program does not update the file since 30 is less than the Hi-score of 45.
# The player scores 50. The program updates the Hi-score in the file to 50.
# This mechanism keeps track of the highest score achieved by any player.
