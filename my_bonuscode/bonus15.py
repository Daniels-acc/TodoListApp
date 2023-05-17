import _json
import json

with open("questions.json", 'r') as file:
    content = file.read()  #always read() for json. content = string type

data = json.loads(content) #data = list file

score = 0
for xy in data:
    print(xy["question_text"])
    for index, alternatives in enumerate(xy["alternatives"]):
        print(f"{index+1}. {alternatives}")
    user_choice = int(input("Enter your answer: ")) + 1
    xy["user_choice"] = user_choice #adding variable user choice with value user_choice to dictionary in questions.json
    if xy["user_choice"] == xy["correct_answer"]: #checking if new user_choice in json == correct_answer
        score = score + 1