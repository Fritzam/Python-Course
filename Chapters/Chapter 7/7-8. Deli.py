sandwich_orders = ["Turkey Club Sandwich", "Italian Submarine Sandwich", "Chicken Avocado Sandwich", "BLT (Bacon, Lettuce, Tomato) Sandwich", "Grilled Cheese Sandwich"]
finished_sandwiches = []

while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print("I've made you a: " + finished_sandwich)
    finished_sandwiches.append(finished_sandwich)

print("All sandwiches have been finished!")