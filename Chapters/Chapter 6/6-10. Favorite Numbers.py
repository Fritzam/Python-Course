import random
rand_number = random.randrange(1, 100)
favorite_numbers = {

    "Ania": [random.randrange(1, 100), random.randrange(1, 100)],
    'Zosia': [random.randrange(1, 100), random.randrange(1, 100)],
    'Gosia': [random.randrange(1, 100), random.randrange(1, 100)]

}

for person, numbers in favorite_numbers.items():
    print("Favorite numbers of " + person + " are: ")
    for number in numbers:
        print(number)


