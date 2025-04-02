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

class Previlegi:
    def __init__(self):
        
        