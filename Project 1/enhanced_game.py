# Here are some additional features you can add to enhance the game and make it more engaging:

# 1. Score Tracking:
# Track the player's wins, losses, and draws across multiple rounds.
import random
def playgame():
    computer = random.choice([-1, 0, 1])  # Computer chooses a random number.
    youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()
    youDict = {"s": 1, "w": -1, "g": 0}  # Map user inputs to numerical values.
    reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}  # Map numerical values to choices for display.

    # Validate user input.
    if youstr not in youDict:
        print("Invalid input! Please choose 's', 'w', or 'g'.")
        return

    you = youDict[youstr]
    print(f"\nYou chose: {reverseDict[you]}")
    print(f"Computer chose: {reverseDict[computer]}")

    # Determine the outcome.
    if computer == you:
        print("It's a draw!")
        return "draw"
    elif (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
        print("You win!")
        return "win"
    else:
        print("You lose!")
        return "lose"

# Score tracking
wins = 0
losses = 0
draws = 0

while True:
    result = playgame()
    
    if result == "win":
        wins += 1
    elif result == "lose":
        losses += 1
    elif result == "draw":
        draws += 1
    
    print(f"\nScores: Wins: {wins}, Losses: {losses}, Draws: {draws}")
    
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break


# 2. Difficulty Levels:
# Add difficulty levels where the computer can choose its move randomly or with a bias (e.g., harder mode where the computer is more likely to win).

def playgame(difficulty="normal"):
    computer_choices = [-1, 0, 1]  # Choices: Water, Gun, Snake
    
    if difficulty == "hard":
        # Harder mode: computer is more likely to choose winning options
        computer = random.choice([0, 1]) if random.random() < 0.75 else random.choice([-1])
    else:
        computer = random.choice(computer_choices)  # Normal mode

    youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()
    youDict = {"s": 1, "w": -1, "g": 0}  # Map user inputs to numerical values.
    reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}  # Map numerical values to choices for display.

    # Validate user input.
    if youstr not in youDict:
        print("Invalid input! Please choose 's', 'w', or 'g'.")
        return

    you = youDict[youstr]
    print(f"\nYou chose: {reverseDict[you]}")
    print(f"Computer chose: {reverseDict[computer]}")

    # Determine the outcome.
    if computer == you:
        print("It's a draw!")
        return "draw"
    elif (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
        print("You win!")
        return "win"
    else:
        print("You lose!")
        return "lose"

difficulty = input("Choose difficulty (normal/hard): ").strip().lower()

# Score tracking
wins = 0
losses = 0
draws = 0

while True:
    result = playgame(difficulty)
    
    if result == "win":
        wins += 1
    elif result == "lose":
        losses += 1
    elif result == "draw":
        draws += 1
    
    print(f"\nScores: Wins: {wins}, Losses: {losses}, Draws: {draws}")
    
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break


# 3. Timer:
# Add a timer that limits how long the player has to choose their move. You can use the time module to implement a countdown.

import time

def playgame():
    computer = random.choice([-1, 0, 1])
    print("\nYou have 10 seconds to make a choice!")
    start_time = time.time()
    
    youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()
    elapsed_time = time.time() - start_time
    
    if elapsed_time > 10:
        print("Time's up! You took too long.")
        return "lose"
    
    youDict = {"s": 1, "w": -1, "g": 0}
    reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

    if youstr not in youDict:
        print("Invalid input! Please choose 's', 'w', or 'g'.")
        return "lose"

    you = youDict[youstr]
    print(f"\nYou chose: {reverseDict[you]}")
    print(f"Computer chose: {reverseDict[computer]}")

    if computer == you:
        print("It's a draw!")
        return "draw"
    elif (computer == -1 and you == 1) or (computer == 1 and you == 0) or (computer == 0 and you == -1):
        print("You win!")
        return "win"
    else:
        print("You lose!")
        return "lose"

# Main game loop with timer
wins = 0
losses = 0
draws = 0

while True:
    result = playgame()
    
    if result == "win":
        wins += 1
    elif result == "lose":
        losses += 1
    elif result == "draw":
        draws += 1
    
    print(f"\nScores: Wins: {wins}, Losses: {losses}, Draws: {draws}")
    
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break


# 4. Play Sound Effects or Music:
# You can use the pygame library or winsound module to play sound effects when the user wins, loses, or draws.

import winsound

def play_sound(choice):
    if choice == "win":
        winsound.Beep(1000, 500)  # Win sound
    elif choice == "lose":
        winsound.Beep(500, 500)  # Lose sound
    elif choice == "draw":
        winsound.Beep(700, 500)  # Draw sound
# Call play_sound(result) after each round to play a sound depending on the result.

# 5. Graphical User Interface (GUI):
# You can use libraries like tkinter to create a GUI where users can click buttons instead of typing their choices.

# 6. Leaderboard:
# Add a leaderboard to track the highest scores or most wins over multiple sessions.

