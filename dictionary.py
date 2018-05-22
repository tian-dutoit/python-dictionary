import json

data = json.load(open("data.json")) 
#  'r' read mode is the default

def meaning(input_word):
    lower_word = input_word.lower()
    if lower_word in data:
       print(data[lower_word])

word = input("Please enter a word: ")

meaning(word)