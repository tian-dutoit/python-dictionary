import json
from difflib import get_close_matches


data = json.load(open("data.json")) 
#  'r' read mode is the default

def meaning(input_word):
    lower_word = input_word.lower()
    if lower_word in data:
        return data[lower_word]
    elif len(get_close_matches(input_word, data.keys())) > 0 :
        closeresponse = input("Did you mean %s? Y/N: " % get_close_matches(input_word, data.keys())[0]).lower()
        if closeresponse == "y":
            newword = data[get_close_matches(input_word, data.keys())[0]]
            return newword
        elif closeresponse == "n":
            return "Word not found"
        else:
            return "Invalid response"

    else:
        return "The word is not in the dictionary"

word = input("Please enter a word: ")

definitions = meaning(word)

if type(definitions) == list:
    for definition in definitions:
        print(definition)
else:
    print(definitions)   
    # if there is a word returned it will be in a list, this loop will print out the different definitions without the [] and on separate lines. If it's not a list it will just print out our string.
    