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
            newword = get_close_matches(input_word, data.keys()[0])
            return newword
        elif closeresponse == "n":
            print("Word not found")
        else:
            print("Invalid response")

    else:
        print("The word is not in the dictionary")


word = input("Please enter a word: ")

print(meaning(word))