# ==================================
# Advanced Number Guessing Game 
# ==================================

import random
import os

BEST_SCORE_FILE = "best_score.txt"


# -------------------------------
# Load Best Score from File
# -------------------------------
def load_best_score():
    if os.path.exists(BEST_SCORE_FILE):
        with open(BEST_SCORE_FILE, "r") as file:
            return int(file.read())
    return None


# -------------------------------
# Save Best Score to File
# -------------------------------
def save_best_score(score):
    with open(BEST_SCORE_FILE, "w") as file:
        file.write(str(score))


# -------------------------------
# Choose Difficulty
# -------------------------------
def choose_difficulty():
    print("\n🎮 Select Difficulty:")
    print("1. Easy (1–10, 5 attempts)")
    print("2. Medium (1–50, 7 attempts)")
    print("3. Hard (1–100, 10 attempts)")

    choice = input("Enter choice (1/2/3): ")

    if choice == "1":
        return 10, 5
    elif choice == "2":
        return 50, 7
    elif choice == "3":
        return 100, 10
    else:
        print("⚠ Invalid choice! Defaulting to Easy.")
        return 10, 5


# -------------------------------
# Game Logic
# -------------------------------
def play_game(player_name, best_score):
    max_number, max_attempts = choose_difficulty()
    secret = random.randint(1, max_number)

    attempts = 0

    print(f"\n🎯 {player_name}, I am thinking of a number between 1 and {max_number}.")

    while attempts < max_attempts:
        try:
            guess = int(input("👉 Enter your guess: "))
            attempts += 1

            if guess == secret:
                score = max_attempts - attempts + 1

                print(f"\n✅ Correct, {player_name}! You guessed it in {attempts} attempts.")
                print(f"🏆 Your Score: {score}")

                # Update best score
                if best_score is None or score > best_score:
                    print("🔥 New Best Score!")
                    save_best_score(score)
                    best_score = score

                return best_score

            elif guess < secret:
                print("📉 Too low!")
            else:
                print("📈 Too high!")

            print(f"Attempts left: {max_attempts - attempts}")

        except ValueError:
            print("⚠ Please enter a valid number!")

    print(f"\n❌ Game Over! The number was {secret}.")
    return best_score


# -------------------------------
# Main Function
# -------------------------------
def main():
    print("🎉 Welcome to the Number Guessing Game!")

    player_name = input("👤 Enter your name: ")

    best_score = load_best_score()

    if best_score:
        print(f"🥇 Best Score so far: {best_score}")

    games_played = 0

    while True:
        best_score = play_game(player_name, best_score)
        games_played += 1

        print(f"\n📊 Games Played: {games_played}")
        if best_score:
            print(f"🥇 Best Score: {best_score}")

        again = input("\nDo you want to play again? (y/n): ").lower()
        if again != "y":
            print(f"\n👋 Thanks for playing, {player_name}!")
            break


# -------------------------------
# Run Game
# -------------------------------
if __name__ == "__main__":
    main()