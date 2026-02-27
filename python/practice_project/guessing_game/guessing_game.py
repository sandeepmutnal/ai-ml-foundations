import random

# Global best score
best_score = None


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


def play_game():
    global best_score

    print("\n🎯 Welcome to the Number Guessing Game!")

    max_number, max_attempts = choose_difficulty()
    secret = random.randint(1, max_number)

    attempts = 0

    print(f"\nI am thinking of a number between 1 and {max_number}.")

    while attempts < max_attempts:
        try:
            guess = int(input("👉 Enter your guess: "))
            attempts += 1

            if guess == secret:
                score = max_attempts - attempts + 1
                print(f"\n✅ Correct! You guessed it in {attempts} attempts.")
                print(f"🏆 Your Score: {score}")

                # Best score update
                if best_score is None or score > best_score:
                    best_score = score
                    print("🔥 New Best Score!")

                return

            elif guess < secret:
                print("📉 Too low!")
            else:
                print("📈 Too high!")

            print(f"Attempts left: {max_attempts - attempts}")

        except ValueError:
            print("⚠ Please enter a valid number!")

    print(f"\n❌ Game Over! The number was {secret}.")


def main():
    print("🎉 Welcome Player!")

    while True:
        play_game()

        print(f"\n🥇 Best Score: {best_score}" if best_score else "")

        again = input("\nDo you want to play again? (y/n): ").lower()
        if again != "y":
            print("👋 Thanks for playing!")
            break


if __name__ == "__main__":
    main()