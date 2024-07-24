""" This module contains Restaurant """
class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restaurant is named " + self.restaurant_name + ", and it serves " + self.cuisine_type + " food.")

    def open_restaurant(self):
        print("Restaurant is now open!")