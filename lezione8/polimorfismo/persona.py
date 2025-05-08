class Persona:
    def __init__(self,name,lastname,age):
        self.set_name(name)
        self.set_lastname(lastname)
        self.set_age(age)

    def __str__(self):
        return f"Nome: {self.name}\nCognome: {self.lastname}\nEtà: {self.age}"
    
    def __call__(self):
        if self.age < 18:
            print(f"{self.name} {self.lastname} e' minorenne!")
        elif 18 <= self.age < 30:
            print(f"{self.name} {self.lastname} e' maggiorenne!")
        elif 30<= self.age < 80:
            print(f"{self.name} {self.lastname} e' una persona adulta!")
        else:
            print(f"{self.name} {self.lastname} e' una persona anziana!")

    def set_name(self, name: str):
        self.name = name

    def set_lastname(self,lastname:str):
        self.lastname=lastname

    def set_age(self,age):
        self.age=age

    def get_name(self):
        return self.name
    
    def get_lastname(self):
        return self.lastname
    
    def get_age(self):
        return self.age
    
    #metodo per la classe persona che simula un saluto
    def speak(self) -> None:
        print (f"\nHello! My name is {self.get_name()}\n")



