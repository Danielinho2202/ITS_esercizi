'''Scrivere un programma che inizializzate due liste a e b della stessa lunghezza n, 
entrambe contenenti valori interi, calcoli la somma incrociata degli elementi.

Esempio:
a[1] + b[n-1], a[2] + b[n-2], ...

Memorizzare ogni somma incrociata in una nuova lista c e, quindi, 
visualizzare in output le liste a, b, c.'''

lista_a:list=[4,7,-3,8,1]
lista_b:list=[-2,0,4,1,-4]

lista_c:list=[(lista_a[0]+lista_b[-1]),(lista_a[1]+lista_b[-2]),(lista_a[2]+lista_b[-3]),(lista_a[3]+lista_b[-4]),(lista_a[4]+lista_b[-5])]
print (lista_c)