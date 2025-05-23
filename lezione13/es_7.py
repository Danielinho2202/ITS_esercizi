'''Una produttoria è definita come il prodotto di un certo numero n di fattori, 
con n intero positivo. Sia Pi3 una produttoria definita come segue:
Pi3 = (1**3) * (2**3) * (3**3) * ... * (n**3)  

Calcolare il valore della produttoria Pi3 se n = 5.'''

def recursivePi3(n:int):
    if n<0:
        return "valore negativo"
    if n==0:
        return 0
    if n==1:
        return n**3
    else:
        return (n**3)*(recursivePi3(n-1))

print (recursivePi3(1))
print (recursivePi3(3))
print (recursivePi3(-5))