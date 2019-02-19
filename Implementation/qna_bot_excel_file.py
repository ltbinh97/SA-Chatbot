import sys
import pandas as pd 
import numbers

df = pd.read_excel('sample_qna.xlxs', sheet_name = 0)

Questions = df['Questions'].tolist()

Answers = df['Answer'].tolist()

print("Hello! I'm here to answer your questions")

def list_faq():
    print("Following some of the most commonly asked questions")
    for i in range(len(Questions)):
        print(str(i)+":"+Questions[i])

def check_for_FAQ_by_index():
    list_faq()
    question_id = input("Which question do you have for me? ")
    respone = ""

    if 'no' in question_id:
        sys.exit()

    if 'bye' in question_id:
        sys.exit()
    elif int(question_id) < len(Questions):
        respone = Answers[int(question_id)]
    else:
        respone = "I don't know the answer to that"
    return respone