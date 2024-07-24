class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("Restaurant is named " + self.restaurant_name + ", and it serves " + self.cuisine_type + " food.")

    def open_restaurant(self):
        print("Restaurant is now open!")

    def set_number_served(self, served):
        self.number_served = served
        print("Current number of customers served is " + str(self.number_served))

    def increment_number_server(self, value):
        self.number_served = self.number_served + value



restaurant = Restaurant("Naru", "Korean")
restaurant.open_restaurant()
restaurant.describe_restaurant()
restaurant.set_number_served(20)
restaurant.increment_number_server(10)
print(restaurant.number_served)
