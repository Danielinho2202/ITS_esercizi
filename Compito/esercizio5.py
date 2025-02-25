'''Si supponga di poter acquistare barrette di cioccolato 
da un distributore automatico al costo di 1 euro ciascuna.
 Ogni barretta acquistata contiene un buono sconto, e con 
 6 buoni sconto si ottiene una barretta gratuita.

Scrivere un programma che:

    Acquisisca in input un valore N (numero di euro disponibili).
    Calcoli e mostri in output il numero totale di barrette che si 
    possono ottenere, considerando anche quelle ottenute con i buoni 
    sconto.
    Mostri quanti buoni sconto avanzano al termine dell'acquisto.'''

N=(int(input("inserisci il numero di euro disponibili: ")))
barrette_di_cioccolato=0
barrette_con_buono=0
while barrette_di_cioccolato<=N:
    if barrette_di_cioccolato%6==0:
        barrette_con_buono+=1
    barrette_di_cioccolato+=1

barrette_di_cioccolato-=1                                           #nell'output non levando le barrette qui e nel rigo 28 veniva sempre due in più, così facendo tutte le prove, è giusto.
barrette_totali= (barrette_di_cioccolato)+(barrette_con_buono)          


while barrette_di_cioccolato>=6:
    barrette_di_cioccolato-=6
print (f"il numero totale di barrette acquistabili è: {barrette_totali-1}")
print (f"al termine dell'acquisto avanzano {barrette_di_cioccolato} buoni")




