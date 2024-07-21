import random

numbers = []
for number in range(1, 6):
    favorite_number = random.randrange(1, 100)
    numbers.append(favorite_number)

people = ['Arek', 'Ryszard', 'Kasia', 'Laura', 'Marta']
dictionary = {'Arek': numbers[0], 'Ryszard': numbers[1], 'Kasia': numbers[2], 'Laura': numbers[3], 'Marta': numbers[4]}
print(dictionary)


