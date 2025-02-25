'''Un'applicazione interessante dei computer è la rappresentazione grafica di dati.
Scrivere un programma che acquisisca cinque numeri interi (ognuno compreso tra 1 e 30)
 e visualizzi in output un grafico a barre testuale con asterischi *.

Per ogni numero letto, il programma deve stampare una riga contenente tanti asterischi 
quanti il valore del numero stesso.'''

numeri:list=[]

for i in range (1,6):
    n=(int(input("inserisci numero asterischi: ")))
    if n>0 and n<=30:
        numeri.append(n)
    else:
        print (f"numero non valido")

for numero in numeri:
    print ("*"*numero)


