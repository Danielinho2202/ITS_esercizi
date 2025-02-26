'''prendi in input una stringa; ogni parola della frase deve iniziare e finire con il maiuscolo'''

'''frase=(str(input("inserisci una frase: "))).title()

print (frase)'''

'''stampare prima e ultima lettera di ogni parola'''

'''frase=(str(input("inserisci una frase: "))).upper


parole=frase.split()

for lettere in parole:
    lettere[0].upper
    lettere[-1].upper
print (parole)'''

#correzione
frase=(str(input("inserisci una frase: ")))
frase= frase.title()
parole= frase.split()
result=[]
for parola in parole:
    p_in = parola [:-1]
    p_ultima = parola[-1]
    nuova = p_in + p_ultima.upper()
    result.append(nuova)
print (" ".join(result))


        



