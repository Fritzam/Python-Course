shado = {
    'type': 'dog',
    'owner': 'Marta'
}

lusia = {
    'type': 'dog',
    'owner': 'Marlena'
}

mia = {
    'type': 'cat',
    'owner': 'Agnieszka'
}

atena = {
    'type': 'chinchila',
    'owner': 'Marlena'
}

gekon = {
    'type': 'lizard',
    'owner': 'Mateusz'
}

pets = [shado, lusia, mia, atena, gekon]
for pet in pets:
    print("You are a little " + pet['type'] +
          ' belonging to ' + pet['owner'] + '.')
