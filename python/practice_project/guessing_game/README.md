# Number Guessing Game (Python)

This is a simple Python mini-project built while learning Python fundamentals.

The program asks the user to guess a secret number and keeps running until the correct number is entered.

---

## Concepts Used
- Variables
- Data types
- Input / Output
- Conditionals (if / else)
- While loop
- Basic debugging mindset

---

## How It Works
1. The program stores a secret number.
2. The user enters a guess.
3. The program checks the guess.
4. If incorrect, it asks again.
5. When correct, it prints "Correct!".

---

## Example Code

```python
secret = 7
guess = 0

while guess != secret:
    guess = int(input("Guess the number: "))

    if guess == secret:
        print("Correct!")
    else:
        print("Try again")
