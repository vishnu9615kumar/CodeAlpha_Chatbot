import datetime

def get_time_based_greeting():
    hour = datetime.datetime.now().hour
    if 5 <= hour < 12:
        return "Good Morning! ☀️"
    elif 12 <= hour < 17:
        return "Good Afternoon! 🌞"
    elif 17 <= hour < 21:
        return "Good Evening! 🌆"
    else:
        return "Good Night! 🌙"

def chatbot():
    print("🤖 Welcome to CodeAlpha Chatbot!")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ["hello", "hi", "hey", "yo", "hello bro"]:
            print(f"Bot: Hi there! {get_time_based_greeting()}")
        elif "how are you" in user_input:
            print("Bot: I'm doing well, how about you?")
        elif "your name" in user_input or "who are you" in user_input:
            print("Bot: I'm CodeAlpha Chatbot 🤖")
        elif "i am fine" in user_input or "i'm fine" in user_input:
            print("Bot: That's great to hear! 😊")
        elif user_input == "bye":
            print("Bot: Goodbye! Have a nice day!")
            break
        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()
