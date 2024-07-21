pizza_toppings = []
while True:
    user_input = input("Please provide requested pizza topping. Write 'quit' to end.")
    if user_input.lower() == 'quit':
        break
    pizza_toppings.append(user_input)

print(pizza_toppings)