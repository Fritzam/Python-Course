favoritePizzas = ["Hot Pepperoni", "Pepperoni", "Mafioso"]

for pizza in favoritePizzas:
    print("I like " + pizza + " pizza.")

print("\nI like pizza very much!")

friendsPizza = favoritePizzas[:]
favoritePizzas.append("Americana")
friendsPizza.append("Hawajska")
print("---------------------")
print(favoritePizzas)
print(friendsPizza)
for pizza in friendsPizza:
    print("My friend's favorite pizza is: " + pizza)