#!/usr/bin/env python3
"""
Simple Natural Language Chatbot
Features: Extended conversation responses and basic interactions
"""

from datetime import datetime
import random

def simple_chatbot():
    print("=" * 50)
    print("Welcome to the Simple Chatbot!")
    print("Type 'quit' or 'exit' to end the conversation.")
    print("=" * 50)
    print()
    
    # Track conversation context
    user_name = None
    
    while True:
        user_input = input("You: ").strip()
        
        if not user_input:
            continue
        
        user_input_lower = user_input.lower()
        
        # Exit commands
        if user_input_lower in ["quit", "exit", "bye", "goodbye"]:
            farewell_messages = [
                "Chatbot: Goodbye! Have a great day!",
                "Chatbot: See you later!",
                "Chatbot: Take care! Bye!"
            ]
            print(random.choice(farewell_messages))
            break
        
        # Greetings
        elif any(word in user_input_lower for word in ["hello", "hi", "hey", "greetings"]):
            if user_name:
                print(f"Chatbot: Hello again, {user_name}! How can I help you?")
            else:
                print("Chatbot: Hello! How can I help you today?")
        
        # How are you
        elif "how are you" in user_input_lower:
            responses = [
                "Chatbot: I'm just a program, but thanks for asking! How are you?",
                "Chatbot: I'm functioning perfectly! How about you?",
                "Chatbot: All systems operational! What brings you here today?"
            ]
            print(random.choice(responses))
        
        # Name introduction
        elif "my name is" in user_input_lower or "i am" in user_input_lower or "i'm" in user_input_lower:
            # Extract name
            words = user_input.split()
            for i, word in enumerate(words):
                if word.lower() in ["is", "am"] and i + 1 < len(words):
                    user_name = words[i + 1].strip(".,!?")
                    print(f"Chatbot: Nice to meet you, {user_name}!")
                    break
        
        # Time query
        elif "time" in user_input_lower:
            now = datetime.now()
            print(f"Chatbot: The current time is {now.strftime('%H:%M:%S')}.")
        
        # Date query
        elif "date" in user_input_lower or "today" in user_input_lower:
            now = datetime.now()
            print(f"Chatbot: Today's date is {now.strftime('%B %d, %Y')}.")
        
        # Day query
        elif "day" in user_input_lower:
            now = datetime.now()
            print(f"Chatbot: Today is {now.strftime('%A')}.")
        
        # Help request
        elif "help" in user_input_lower:
            print("Chatbot: I can help you with:")
            print("  - Telling you the current time, date, or day")
            print("  - Having a friendly conversation")
            print("  - Answering basic questions")
            print("  - Telling jokes")
            print("  What would you like to know?")
        
        # Jokes
        elif "joke" in user_input_lower or "funny" in user_input_lower:
            jokes = [
                "Why don't programmers like nature? It has too many bugs!",
                "Why do programmers prefer dark mode? Because light attracts bugs!",
                "What's a programmer's favorite place? The Foo Bar!",
                "Why did the developer go broke? Because he used up all his cache!",
                "How many programmers does it take to change a light bulb? None, that's a hardware problem!"
            ]
            print(f"Chatbot: {random.choice(jokes)}")
        
        # Weather (simulated)
        elif "weather" in user_input_lower:
            print("Chatbot: I don't have real-time weather data, but you can check weather.com or your local weather service!")
        
        # Thank you
        elif "thank" in user_input_lower:
            responses = [
                "Chatbot: You're welcome!",
                "Chatbot: Happy to help!",
                "Chatbot: Anytime! 😊"
            ]
            print(random.choice(responses))
        
        # Age question
        elif "how old" in user_input_lower or "your age" in user_input_lower:
            print("Chatbot: I was created recently, so I'm pretty young in computer terms!")
        
        # What can you do
        elif "what can you do" in user_input_lower or "your abilities" in user_input_lower:
            print("Chatbot: I can chat with you, tell you the time and date, share jokes, and answer basic questions!")
        
        # Name of chatbot
        elif "your name" in user_input_lower or "who are you" in user_input_lower:
            print("Chatbot: I'm a simple chatbot created to have friendly conversations with you!")
        
        # Math questions (basic)
        elif any(op in user_input for op in ["+", "-", "*", "/"]):
            try:
                result = eval(user_input)
                print(f"Chatbot: The answer is {result}")
            except:
                print("Chatbot: I couldn't calculate that. Try a simple expression like '5 + 3'")
        
        # Default response
        else:
            default_responses = [
                "Chatbot: I didn't understand that. Can you rephrase?",
                "Chatbot: Interesting! Could you tell me more?",
                "Chatbot: I'm not sure about that. Can you ask something else?",
                "Chatbot: That's beyond my knowledge. Try asking about time, date, or jokes!"
            ]
            print(random.choice(default_responses))

if __name__ == "__main__":
    simple_chatbot()
