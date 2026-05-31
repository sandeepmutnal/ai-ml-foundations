# Project 8
# GUI AI Assistant

import tkinter as tk
from tkinter import scrolledtext
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


# Knowledge Base

questions = [
    "hello",
    "hi",
    "how are you",
    "what is python",
    "what is ai",
    "what is machine learning",
    "what is data science",
    "how to get a software job",
    "help me",
    "bye"
]

responses = [
    "Hello! Nice to meet you.",
    "Hi! How can I help you?",
    "I am doing well.",
    "Python is a popular programming language.",
    "AI means Artificial Intelligence.",
    "Machine Learning helps computers learn from data.",
    "Data Science extracts insights from data.",
    "Build projects, learn DSA, and practice coding interviews.",
    "I am here to help you.",
    "Goodbye!"
]


# TF-IDF

vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)


# Chat Function

def send_message():

    user_message = entry.get()

    if not user_message.strip():
        return

    chat_area.insert(tk.END, f"You: {user_message}\n")

    user_vector = vectorizer.transform([user_message])

    similarity = cosine_similarity(
        user_vector,
        question_vectors
    )

    best_match = np.argmax(similarity)

    best_score = similarity[0][best_match]

    if best_score > 0.3:
        bot_response = responses[best_match]
    else:
        bot_response = "Sorry, I don't understand that yet."

    chat_area.insert(tk.END, f"Bot: {bot_response}\n\n")

    entry.delete(0, tk.END)


# GUI Window

window = tk.Tk()
window.title("AI Assistant")
window.geometry("600x500")


# Chat Area

chat_area = scrolledtext.ScrolledText(
    window,
    wrap=tk.WORD,
    width=70,
    height=20
)

chat_area.pack(pady=10)


# Input Frame

frame = tk.Frame(window)
frame.pack()


entry = tk.Entry(frame, width=50)
entry.pack(side=tk.LEFT, padx=5)


send_button = tk.Button(
    frame,
    text="Send",
    command=send_message
)

send_button.pack(side=tk.LEFT)


# Run App

window.mainloop()