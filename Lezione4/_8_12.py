'''Write a function that accepts a list of items a person wants on a sandwich. 
The function should have one parameter that collects as many items as the function call provides,
 and it should print a summary of the sandwich that’s being ordered.
 Call the function three times, using a different number of arguments each time.'''


def sandwich(*args):
    ingredienti=list(args)
    for ingrediente in ingredienti:
        print (f"- {ingrediente}")

sandwich("pomodoro","tonno","formaggio")
sandwich("formaggio","prosciutto","salame")
sandwich("broccoli","salsiccia")
