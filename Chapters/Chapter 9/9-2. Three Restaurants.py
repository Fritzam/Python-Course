class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant is named " + self.restaurant_name + ", and it serves " + self.cuisine_type + " food.")

    def open_restaurant(self):
        print("Restaurant is now open!")


restaurant = Restaurant("Naru", "Korean")
restaurant.open_restaurant()
restaurant.describe_restaurant()
kebab = Restaurant("Kebab King", "Oriental")
kebab.open_restaurant()
kebab.describe_restaurant()
elMuchoLoco = Restaurant("ElMuchoLoco", "Mexian")
elMuchoLoco.open_restaurant()
elMuchoLoco.describe_restaurant()
