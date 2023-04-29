class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Our restaurant name is {self.restaurant_name} and it is an {self.cuisine_type} food restaurant")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open now")


my_restaurant = Restaurant("SarabLohee", "Italian")
my_restaurant.describe_restaurant()
my_restaurant1 = Restaurant("Veerji Chaamp Wale", "North Indian")
my_restaurant1.describe_restaurant()
my_restaurant2 = Restaurant("Hira Sweets", "Desi")
my_restaurant2.describe_restaurant()


