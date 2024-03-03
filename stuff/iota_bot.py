import json
chat_dict_code = "chat_dict.json"
with open(chat_dict_code) as f:
    chat_dict = json.load(f)
    
last_answers_code = "last_answers.json"
with open(last_answers_code) as f:
    last_answers = json.load(f)

name = "noname"
last_answer = "nothing"

def formate(string): #Macht deine Frage grammatikalisch fragwürdig + lesbar
    newstring = ""
    prohibited_letters = [".", ",", "!", "?", ":", ";", "§"]
    string = string.strip()
    lastspace = False
    for letter in string:
        if not letter in prohibited_letters:
            if lastspace and letter == " ":
                continue
            newstring = newstring + letter
            if letter == " ":
                lastspace = True
            else:
                lastspace = False
    return newstring
                  
def answer(question, last_answers = {}):
    global last_answer
    question = formate(question)
    words = question.split()
    numbers = []
    for word in words:
        if isinstance(word, float):
            numbers.append(word)
    if not question in chat_dict: #im Fragenkatalog vorhanden
        if question == "ende" or question == "tschüss" or question == "bye":
            print(f"Iota: Einen schönen Tag noch, {name}!")
            return 0
        try:
            print(f"Iota: {last_answers.get(last_answer).get(question)}")
        except AttributeError:
            pass
        
    else:
        if chat_dict[question].rstrip() == chat_dict[question]: #Name benutzen
            print(f"Iota: {chat_dict[question]}")
            last_answer = chat_dict[question]
        else:
            print(f"Iota: {chat_dict[question]}{name}!")
    return 1

name = input("Iota: Hallo! Wie heißt du denn?  ")
print()
print(f"Iota: Cool! Was liegt dir denn auf dem Herzen, {name}?")
running = 1
while running:
    running = answer(input(f"      {name}: ").lower(), last_answers)
    
    

    
    
    
    
        

        

        
    


  



