def question_finder(sentence):
    parameters = ("when","why","who","how","what")
    capital = sentence.capitalize()
    if(sentence.startswith(parameters)):
        return "{}?".format(capital)
    else:
        return "{}.".format(capital)

    return capital

data = []

while True:
    yourdata = input("Type a Sentence:")
    if(yourdata == "stop"):
        break
    else:
        data.append(question_finder(yourdata))

print(" ".join(data))

#print(question_finder("do you eat"))