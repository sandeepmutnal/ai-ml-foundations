# Project 8
# NLP Preprocessing Chatbot

import string


print("🤖 AI Chatbot Started")
print("Type 'bye' to stop the chatbot\n")


while True:

    # User Input

    user_input = input("You: ")


    # Convert to lowercase

    user_input = user_input.lower()


    # Remove punctuation

    user_input = user_input.translate(
        str.maketrans('', '', string.punctuation)
    )


    # Chatbot Responses

    if user_input == "hello":
        print("Bot: Hello! Welcome!")

    elif user_input == "how are you":
        print("Bot: I am fine. Thank you!")

    elif user_input == "what is your name":
        print("Bot: I am an AI chatbot.")

    elif user_input == "python":
        print("Bot: Python is a powerful programming language.")

    elif user_input == "help":
        print("Bot: I can answer simple questions.")

    elif user_input == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I do not understand.")