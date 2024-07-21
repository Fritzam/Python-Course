cities = {
    'Gdańsk': {
        'country': 'Poland',
        'population': 420000,
        'fact': 'Used to be the wealthiest city in Poland'
    },

    'London': {
        'country': 'England',
        'population': 8799800,
        'fact': 'Vampyr game takes place here.'
    },

    'Tokio': {
        'country': 'Japan',
        'population': 14064696,
        'fact': 'Most populous city on Earth'
    }
}

for city, data in cities.items():
    print(city + " lies in country of: " + data['country'] +
          ', with population of: ' + str(data['population']) + '.\n' +
          'A trivia about this city is that: ' + data['fact'] + '.')