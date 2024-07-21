person = {
    'name': 'Marta',
    "surname": 'REDACTED',
    'city': 'Wrocław'
}
person2 = {
    'name': 'Mateusz',
    'surname': 'REDACTED',
    'city': 'Gdańsk'
}
person3 = {
    'name': "Łukasz",
    'surname': 'REDACTED',
    'city': 'Kraków'
}

people = [person, person2, person3]
for person in people:
    print("You are my friend " + person['name'] +
          ", and You are from " + person['city'] +
          '.')