import random

# Predefined responses
responses = {
    "hello": [
        "Hello! How can I help you?",
        "Hi there! Nice to meet you.",
        "Hey! How are you doing?"
    ],
    "how are you": [
        "I'm fine, thanks for asking!",
        "I'm doing great! How about you?",
        "I'm just a chatbot, but I'm doing well!"
    ],
    "your name": [
        "I'm Python Bot!",
        "You can call me PyBot.",
        "I'm your friendly chatbot."
    ],
    "help": [
        "Sure! Tell me what you need help with.",
        "I'm here to help. Ask me something!",
        "Of course! What do you need?"
    ],
    "bye": [
        "Goodbye! Have a great day!",
        "See you later!",
        "Bye! Take care."
    ]
}

print("=" * 40)
print("       WELCOME TO PYTHON CHATBOT")
print("=" * 40)
print("You can chat with me!")
print("Type 'bye' to exit the conversation.\n")

# Main chatbot loop
while True:
    user_input = input("You: ").lower().strip()

    # Exit the chatbot
    if "bye" in user_input:
        print("Bot:", random.choice(responses["bye"]))
        break

    # Check user input and respond
    elif "hello" in user_input or "hi" in user_input or "hey" in user_input:
        print("Bot:", random.choice(responses["hello"]))

    elif "how are you" in user_input:
        print("Bot:", random.choice(responses["how are you"]))

    elif "your name" in user_input or "who are you" in user_input:
        print("Bot:", random.choice(responses["your name"]))

    elif "help" in user_input:
        print("Bot:", random.choice(responses["help"]))

    elif user_input == "":
        print("Bot: Please type something!")

    else:
        print("Bot: Sorry, I don't understand that. Try asking something else!")
