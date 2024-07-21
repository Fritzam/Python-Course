sandwich_orders = ["Turkey Club Sandwich", "Italian Submarine Sandwich", "Chicken Avocado Sandwich", "Turkey Club Sandwich", "BLT (Bacon, Lettuce, Tomato) Sandwich", "Turkey Club Sandwich", "Grilled Cheese Sandwich"]
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    if sandwich != "Turkey Club Sandwich":
        print("I've made you a: " + sandwich)
        finished_sandwiches.append(sandwich)

print(finished_sandwiches)
