class Restaurant:

    def __init__(self, restaurant_name, cuisine_type, number_served=0):

        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served


    def describe_restaurant(self):
        print (f"{self.restaurant_name}: {self.cuisine_type}\nnumber served: {self.number_served}")

    def open_restaurant(self):
        print ("open")

    def set_number_served(self,number_served):
        self.number_served = number_served

    def increment_number_served(self,add_number_served):
        self.number_served=self.number_served+add_number_served

    


alice_pizza= Restaurant("Alice Pizza", "Pizzeria")
alice_pizza.describe_restaurant()
alice_pizza.open_restaurant()
print("---------------------")
alice_pizza.set_number_served(3)
alice_pizza.describe_restaurant()
print("---------------------")
alice_pizza.increment_number_served(10)
alice_pizza.describe_restaurant()
print("-----------------------")
alice_pizza.increment_number_served(20)
alice_pizza.describe_restaurant()



