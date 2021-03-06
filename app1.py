import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys())) > 0:
        return "Did you mean %s instead?" %get_close_matches(word, data.keys())[0]
    else:
        return "That word doesn't exits, please double check it."

word = input("Enter a word: ")

print(translate(word))
