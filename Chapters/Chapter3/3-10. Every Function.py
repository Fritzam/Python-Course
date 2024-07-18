countries = ["France", "United Kingdom", "Poland", "USA", "Japan", "Russia", "Korea"]
countries.remove("Russia")  # too cold
napoleon = countries.pop(0)
del countries[1]
print(countries)
countries.insert(0, "Poland")
countries.append(napoleon)
print(countries)
countries.sort()
print(countries)
countries.reverse()
print(countries)
print(sorted(countries))
