'''
    Create a function that defines a product with a name, price, and quantity.
     Create a function that manages the shopping cart, allowing the user to add, remove, and view products in the cart.
    The function should calculate the cart total and apply any discounts or taxes.
     Implement a for loop to iterate over the items in the cart and print detailed information about each product and the total.
'''

def crea_prodotto(nome:str,prezzo:float,quantità:int):
    prodotto= {"nome":nome,"prezzo":prezzo,"quantità":quantità}
    return prodotto

carrello=[]
def aggiungi_al_carrello(prodotto):
    carrello.append(prodotto)


def rimuovi_dal_carrello (prodotto):
    for item in carrello:
        if item['nome']==prodotto['nome']:
            carrello.remove(prodotto)



def visualizza_carrello(carrello):
    for prodotto in carrello:
        print (f"nome: {prodotto['nome']}, prezzo: {prodotto['prezzo']}$, quantità: {prodotto['quantità']}")


def totale_carrello(carrello,sconto=None,tasse=10):
    somma=0
    for prodotto in carrello:
        somma=somma+(prodotto['prezzo'] * prodotto ['quantità'])
    
    print (f"{somma}$")


aggiungi_al_carrello(crea_prodotto("pasta",2.0,3))
aggiungi_al_carrello(crea_prodotto("tonno",2.0,3))
visualizza_carrello(carrello)
totale_carrello(carrello)
rimuovi_dal_carrello(crea_prodotto("pasta",2.0,3))
visualizza_carrello(carrello)



