try:
    with open('Cats.txt') as cats:
        print(cats.read())
    with open('Dogs.txt') as dogs:
        print(dogs.read())
except FileNotFoundError:
    print("File does not exist!")