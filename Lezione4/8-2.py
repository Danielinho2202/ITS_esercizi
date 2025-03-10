'''Write a function called favorite_book() that accepts one parameter, title. 
The function should print a message, such as "One of my favorite books is Alice in Wonderland".
 Call the function, making sure to include a book title as an argument in the function call.'''


def libro_preferito(title):
    print (f"il mio libro preferito è {title}!")

title = str(input("qual'è il tuo libro preferito? "))
libro_preferito(title)