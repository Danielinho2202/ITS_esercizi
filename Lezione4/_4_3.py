'''
    Create a function that defines a product with a name, price, and quantity.
     Create a function that manages the shopping cart, allowing the user to add, remove, and view products in the cart.
    The function should calculate the cart total and apply any discounts or taxes.
     Implement a for loop to iterate over the items in the cart and print detailed information about each product and the total.
'''

def shopping_cart(azione,nome=None,prezzo=None,quantita=None):
    carrello:dict={}
    while True:
        match azione:
            case "aggiungi":
                carrello[nome]= prezzo

            
