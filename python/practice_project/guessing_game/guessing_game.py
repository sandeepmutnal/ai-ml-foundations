# ==================================
# Advanced GUI Number Guessing Game (Day 5 - Pro Version)
# ==================================

import tkinter as tk
from tkinter import ttk
import random
import os
import json

DATA_FILE = "game_data.json"


# -------------------------------
# File Handling
# -------------------------------
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {"best_score": 0, "wins": 0, "losses": 0}


def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file)


# -------------------------------
# Game Class
# -------------------------------
class AdvancedGame:

    def __init__(self, root):
        self.root = root
        self.root.title("🎯 Advanced Guessing Game")
        self.root.geometry("450x550")

        self.data = load_data()

        self.best_score = self.data["best_score"]
        self.wins = self.data["wins"]
        self.losses = self.data["losses"]

        self.timer_id = None
        self.game_active = True

        self.dark_mode = False

        self.create_widgets()
        self.start_game()

    # ---------------- UI ----------------
    def create_widgets(self):

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(pady=10)

        self.title = tk.Label(self.main_frame,
                              text="🎯 Guess The Number",
                              font=("Arial", 18, "bold"))
        self.title.pack(pady=10)

        tk.Label(self.main_frame, text="Select Difficulty").pack()

        self.difficulty = ttk.Combobox(
            self.main_frame,
            values=["Easy", "Medium", "Hard"],
            state="readonly")
        self.difficulty.current(0)
        self.difficulty.pack(pady=5)

        self.info_label = tk.Label(self.main_frame, text="")
        self.info_label.pack()

        self.timer_label = tk.Label(
            self.main_frame,
            text="⏱ Time: 30",
            font=("Arial", 12, "bold"))
        self.timer_label.pack()

        self.entry = tk.Entry(self.main_frame, font=("Arial", 14))
        self.entry.pack(pady=10)

        self.entry.bind("<Return>", lambda e: self.check_guess())

        self.result_label = tk.Label(self.main_frame, text="", font=("Arial", 12))
        self.result_label.pack()

        self.attempt_label = tk.Label(self.main_frame, text="")
        self.attempt_label.pack()

        self.stats_label = tk.Label(self.main_frame, text="")
        self.stats_label.pack()

        self.best_label = tk.Label(
            self.main_frame,
            text=f"🥇 Best Score: {self.best_score}")
        self.best_label.pack()

        self.guess_button = tk.Button(
            self.main_frame,
            text="Guess",
            command=self.check_guess,
            bg="#4CAF50",
            fg="white")
        self.guess_button.pack(pady=5)

        tk.Button(
            self.main_frame,
            text="New Game",
            command=self.start_game,
            bg="#2196F3",
            fg="white").pack(pady=5)

        tk.Button(
            self.main_frame,
            text="Toggle Dark Mode 🌙",
            command=self.toggle_theme).pack(pady=5)

    # ---------------- Theme ----------------
    def toggle_theme(self):

        if self.dark_mode:
            bg = "#f0f4f8"
            fg = "black"
            self.dark_mode = False
        else:
            bg = "#1e1e1e"
            fg = "white"
            self.dark_mode = True

        self.root.configure(bg=bg)
        self.main_frame.configure(bg=bg)

        for widget in self.main_frame.winfo_children():
            try:
                widget.configure(bg=bg, fg=fg)
            except:
                pass

    # ---------------- Game Setup ----------------
    def start_game(self):

        if self.timer_id:
            self.root.after_cancel(self.timer_id)

        level = self.difficulty.get()

        if level == "Easy":
            self.max_number = 10
            self.max_attempts = 5

        elif level == "Medium":
            self.max_number = 50
            self.max_attempts = 7

        else:
            self.max_number = 100
            self.max_attempts = 10

        self.secret = random.randint(1, self.max_number)

        self.attempts = 0
        self.time_left = 30
        self.game_active = True

        self.entry.config(state="normal")
        self.guess_button.config(state="normal")

        self.entry.delete(0, tk.END)

        self.result_label.config(text="")
        self.info_label.config(text=f"Guess between 1 and {self.max_number}")

        self.update_attempts()
        self.update_stats()

        self.run_timer()

    # ---------------- Timer ----------------
    def run_timer(self):

        if not self.game_active:
            return

        if self.time_left > 0:

            self.timer_label.config(text=f"⏱ Time: {self.time_left}")
            self.time_left -= 1

            self.timer_id = self.root.after(1000, self.run_timer)

        else:

            self.losses += 1
            self.end_game(False, "⏰ Time's Up!")

    # ---------------- Guess Logic ----------------
    def check_guess(self):

        if not self.game_active:
            return

        try:

            guess = int(self.entry.get())
            self.entry.delete(0, tk.END)

            self.attempts += 1

            if guess == self.secret:

                score = self.max_attempts - self.attempts + 1

                self.wins += 1

                if score > self.best_score:
                    self.best_score = score
                    self.data["best_score"] = score

                self.end_game(True, f"✅ Correct! Score: {score}")

            elif guess < self.secret:
                self.result_label.config(text="📉 Too Low!")

            else:
                self.result_label.config(text="📈 Too High!")

            self.update_attempts()

            if self.attempts >= self.max_attempts:

                self.losses += 1
                self.end_game(False,
                              f"❌ Game Over! Number was {self.secret}")

        except ValueError:

            self.result_label.config(text="⚠ Enter a valid number!")

    # ---------------- End Game ----------------
    def end_game(self, win, message):

        self.game_active = False

        self.result_label.config(text=message)

        self.entry.config(state="disabled")
        self.guess_button.config(state="disabled")

        if self.timer_id:
            self.root.after_cancel(self.timer_id)

        self.update_stats()

        self.data["wins"] = self.wins
        self.data["losses"] = self.losses

        save_data(self.data)

    # ---------------- Updates ----------------
    def update_attempts(self):

        remaining = self.max_attempts - self.attempts

        self.attempt_label.config(text=f"Attempts Left: {remaining}")

    def update_stats(self):

        total = self.wins + self.losses

        win_rate = (self.wins / total) * 100 if total > 0 else 0

        self.stats_label.config(
            text=f"📊 Wins: {self.wins} | Losses: {self.losses} | Win Rate: {win_rate:.1f}%")

        self.best_label.config(text=f"🥇 Best Score: {self.best_score}")


# ---------------- Run App ----------------
if __name__ == "__main__":

    root = tk.Tk()

    game = AdvancedGame(root)

    root.mainloop()