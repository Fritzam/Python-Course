rivers_list = {
    'Nile': 'Egypt',
    'Vistula': "Poland",
    'Thames': 'England',
    'Sequana': 'France',
    'Volga': 'Russia'
}

for river, country in sorted(rivers_list.items()):
    print("The " + river + " runs through " + country + ".")