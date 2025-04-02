class User:
    def __init__(self,first_name,last_name,age,residence,login_attempt):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.residence=residence
        self.login_attempt=login_attempt
        self.login_attempt_counter=0


    def describe_user(self):
        print (f"first name: {self.first_name}\nlast name: {self.last_name}\n" 
               f"age: {self.age}\nresidence: {self.residence}")
        
    
    def greet_user(self):
        print (f"hi, {self.first_name}!")

    def increment_login_attempt(self):
        if self.login_attempt==1:
            self.login_attempt_counter+=1
    
    def reset_login_attempt(self):
        if self.login_attempt==0:
            self.login_attempt_counter=0


user1=User("Daniele","Gallo","21","Roma",1)
#user1.describe_user()
#user1.greet_user()
print (user1.login_attempt_counter)