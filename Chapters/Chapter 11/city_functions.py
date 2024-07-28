def full_location(city, country, population=""):
    if population:
        return city.title() + ", " + country.title() + ", " + str(population)
    else:
        return city.title() + ", " + country.title()
