class User:
    def __init__(self,first_name,last_name,username,email):
        self.first_name=first_name
        self.last_name=last_name
        self.username=username
        self.email=email


    def describe_user(self):
        print (f"first name: {self.first_name}\nlast name: {self.last_name}\n" 
               f"username: {self.username}\nemail: {self.email}")
        
    
    def greet_user(self):
        print (f"hi, {self.first_name}!")


user1=User("Daniele","Gallo","21","Roma")
user1.describe_user()
user1.greet_user()
user2=User("Yao Kouassi", "Gervinho", 35,"Yamoussoukro")
user2.describe_user()
user2.greet_user()




