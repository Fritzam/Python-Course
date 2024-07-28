import json

with open('favorite_number.txt') as number:
    number = json.load(number)
    print("Your favorite number is: " + number)