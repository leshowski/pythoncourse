import json
from difflib import get_close_matches

elements = json.load(open("wordbook.json"))

def findmeaning(word):
    if word.lower() in elements:
        return elements[word.lower()]
    elif word.upper() in elements:
        return elements[word.upper()]
    elif word.title() in elements:
        return elements[word.title()]    
    elif len(get_close_matches(word,elements.keys()))>0:
        close_matches = (get_close_matches(word,elements.keys())[0])

        user_decision = input("Are you looking for %s instead? [Y/N]" % close_matches)

        if user_decision.lower() == "y":
            return elements[get_close_matches(word,elements.keys())[0]]
        elif user_decision.lower() == "n":
            return "No encontrado"

    else:
        return "No encontrado"

word = input("Ingrese palabra a buscar:")

output = findmeaning(word)

if type(output) == list:
    for i in output:
        print(i)
else:
    print(output)
