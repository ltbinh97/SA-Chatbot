import random
import sys

Questions = [
    "How are you?",
    "What are you doing?",
    "How is the weather today?"
]

Answers = [
    "I'm fine thank you!",
    "Nothing interesting.",
    "The weather is nice"
]

def list_faq():
    for i in range(len(Questions)):
        print(str(i) + ":" + Questions[i])

def check_for_FAQ_by_index():
    list_faq()
    question_id = input("Which question do you want me to answer? ")
    respone = ""

    if 'bye' in question_id:
        sys.exit()
    elif int(question_id) < len(Questions):
        respone = Answers[int(question_id)]
    else:
        respone = "I don't know the answer to that"
    return respone

def check_for_FAQ(question):
    respone = ""
    if question in Questions:
        index = Questions.index(question)
        respone = Answers[index]
    else:
        respone = "I don't know answer to that"
    return respone

while True:
    respone = check_for_FAQ_by_index()
    print("Your Bot: " + respone)