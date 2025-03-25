class Student:

    def __init__(self,name,study_program,age,gender):

        self.name=name
        self.study_program=study_program
        self.age=age
        self.gender=gender

    def print_info (self):
        
        print (f"name: {self.name}; study program: {self.study_program}; "
        f"age: {self.age}; gender: {self.gender}")
    
Daniele= Student("Daniele","Cloud","21","uomo")
Daniele.print_info()

