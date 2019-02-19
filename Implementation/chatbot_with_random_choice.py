import random

Greeting_words = ("hello", "hi", "ssup", "greetings")
Greeting_response = ["hey", "Good morning", "Wassup"]

def check_for_greeting(sentence):
    for word in sentence.split(' '):
        if word.lower() in Greeting_words:
            return random.choice(Greeting_response)
        else:
            return "I don't know what you are talking about"

while True:
    sentence = input("You: ")
    response = check_for_greeting(sentence)
    print("Your bot: " + response)

    if 'bye' in sentence:
        break
    
