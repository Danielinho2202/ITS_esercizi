'''Scrivere un programma che acquisisca in input due numeri interi, n1 e n2, 
e calcoli il prodotto di tutti i numeri compresi tra n1 e n2, inclusi gli estremi.

Il programma deve gestire anche il caso in cui n1 > n2, calcolando comunque
il prodotto correttamente.'''

n1= (int(input("inserisci un numero: ")))
n2= (int(input("inserisci un altro numero: ")))
prodotto=1
if n2>=n1:                                      #verifico quali dei due numeri è maggiore
    for number in range (n1,n2+1):
        prodotto= prodotto*number
if n2<n1:
    for number in range (n2,n1+1):
        prodotto= prodotto*number

print (prodotto)
