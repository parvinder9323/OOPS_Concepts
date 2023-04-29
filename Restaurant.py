class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Our restaurant name is {self.restaurant_name} and it is an {self.cuisine_type} food restaurant")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open now")


my_restaurant = Restaurant("SarabLohee", "Italian")
print(f"Our Rest name is {my_restaurant.restaurant_name}")
print(f"Our cuisine is {my_restaurant.cuisine_type}")

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

