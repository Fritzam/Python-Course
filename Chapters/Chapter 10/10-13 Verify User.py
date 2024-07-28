import json


def create_new_user():
    username = input("Please input Your username")
    with open('user.txt', 'w') as user:
        json.dump(username, user)
        print("We will remember You next time You'll be back!")


try:
    with open('user.txt') as user:
        username = json.load(user)
        response = input("Is '" + username + "' Your username? y/n")
        if response == 'y':
            print("Welcome back " + username + "!")
        else:
            create_new_user()
except FileNotFoundError:
    create_new_user()

