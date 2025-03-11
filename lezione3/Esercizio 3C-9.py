'''Scrivere un programma in Python che permetta all'utente di inserire le coordinate di un punto (x, y) e salvi le coordinate inserite in una tupla.
 Utilizzare il  match statement per determinare la sua posizione del punto inserito nel piano cartesiano:

- Origine → Se il punto è (0,0), stampare: "Il punto si trova nell'origine."
- Asse X → Se y = 0, stampare: "Il punto si trova sull'asse X."
- Asse Y → Se x = 0, stampare: "Il punto si trova sull'asse Y."
- Primo quadrante → Se x > 0 e y > 0, stampare: "Il punto si trova nel primo quadrante."
- Secondo quadrante → Se x < 0 e y > 0, stampare: "Il punto si trova nel secondo quadrante."
- Terzo quadrante → Se x < 0 e y < 0, stampare: "Il punto si trova nel terzo quadrante."
- Quarto quadrante → Se x > 0 e y < 0, stampare: "Il punto si trova nel quarto quadrante."

Expected Output:

Inserisci la coordinata X: 0
Inserisci la coordinata Y: 0
Output: Il punto (0,0) si trova nell'origine.'''

x=float(input("inserisci x= "))
y=float(input("inserisci y= "))

coordinate:tuple=(x,y)

match coordinate:
    case (0,0):
        print ("il punto si trova nell'origine")
    case (x,0):
        print ("il punto si trova sull'asse x")
    case (0,y):
        print ("il punto è sull'asse y")
    case (x,y) if x<0 and y<0:
        print ("terzo quadrante")
    case (x,y) if x>0 and y>0:
        print ("primo quadrante")
    case (x,y) if x<0 and y>0:
        print ("secondo quadrante")
    case (x,y) if x>0 and y<0:
        print ("quarto quadrante")


