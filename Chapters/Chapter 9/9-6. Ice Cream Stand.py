class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant is named " + self.restaurant_name + ", and it serves " + self.cuisine_type + " food.")

    def open_restaurant(self):
        print("Restaurant is now open!")


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type="Ice Cream"):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['Cherry', 'Gum', 'Raspberry', 'Coffee', 'Chocolate']

    def print_flavors(self):
        for flavor in self.flavors:
            print(flavor)


restaurant = Restaurant("Naru", "Korean")
restaurant.open_restaurant()
restaurant.describe_restaurant()
iceCream = IceCreamStand('FamilyIceCream')
iceCream.describe_restaurant()
iceCream.print_flavors()