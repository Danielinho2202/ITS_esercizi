class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print (f"{self.restaurant_name}:{self.cuisine_type}")

    def open_restaurant(self):
        print ("open")


alice_pizza= Restaurant("Alice Pizza", "Pizzeria")
sushiko= Restaurant("Sushiko","Giapponese")
alice_pizza.describe_restaurant()
alice_pizza.open_restaurant()
sushiko.describe_restaurant()
sushiko.open_restaurant()

        
