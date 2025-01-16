'''Enhanced Features
Input Validation:
Ensures the user enters a number within the valid range (1–100).
Attempt Limit:
Limits the number of attempts to 10. If the user exceeds the limit, the game ends.
Difficulty Levels:
Allows the user to choose difficulty levels (Easy, Medium, Hard), which affect the range of the random number and the number of allowed attempts.
Replay Option:
After a game ends, the user can choose to play again.'''

import random

def play_game():
    print("Welcome to the Guess the Number Game!")
    print("Choose a difficulty level:")
    print("1. Easy (1-50, 15 attempts)")
    print("2. Medium (1-100, 10 attempts)")
    print("3. Hard (1-200, 7 attempts)")

    difficulty = int(input("Enter your choice (1/2/3): "))
    
    if difficulty == 1:
        n = random.randint(1, 50)
        max_attempts = 15
    elif difficulty == 2:
        n = random.randint(1, 100)
        max_attempts = 10
    elif difficulty == 3:
        n = random.randint(1, 200)
        max_attempts = 7
    else:
        print("Invalid choice! Defaulting to Medium difficulty.")
        n = random.randint(1, 100)
        max_attempts = 10

    print(f"Guess the number! You have {max_attempts} attempts.")
    
    attempts = 0
    while attempts < max_attempts:
        try:
            a = int(input("Enter your guess: "))
            
            # Validate the input range
            if a < 1 or a > (50 if difficulty == 1 else 100 if difficulty == 2 else 200):
                print(f"Please guess a number within the valid range!")
                continue

            attempts += 1

            if a > n:
                print("Lower number, please!")
            elif a < n:
                print("Higher number, please!")
            else:
                print(f"Congratulations! You guessed the number {n} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    if attempts == max_attempts and a != n:
        print(f"Game Over! You've used all {max_attempts} attempts. The number was {n}.")
    
    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        play_game()
    else:
        print("Thanks for playing! Goodbye.")

# Start the game
play_game()


# strip() ensures no accidental spaces before or after the input affect the response.
# lower() makes the input case-insensitive, so users can type "YES", "yes", "yEs", etc., and it will all be treated as "yes".