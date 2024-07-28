import json

fav_number = input("What is your favorite number?")
with open('favorite_number.txt', 'w') as fav:
    json.dump(fav_number, fav)
    print("We will remember Your favorite number"
          "the next time You'll come back!")
