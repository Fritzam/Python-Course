favorite_places = {
    'Marta': ['Energylandia', 'Wrocław', 'Etno'],
    'Dawid': ['Anywhere outside Poland'],
    'Mateusz': ['Lwów', 'Czernobyl']
}
for person, places in favorite_places.items():
    print('-----------------')
    print(person + " lubi przebywać w: ")
    for place in places:
        print(place)
print('-----------------')
