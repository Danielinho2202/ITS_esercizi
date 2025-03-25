'''
    Create a function that generates a random number within a range specified by the user.
    Prompt the user to guess the number within a specified maximum number of attempts.
    Provide feedback to the user after each guess, indicating whether their guess is too high, too low, or correct.
    Terminate the loop when the user guesses the number correctly or reaches the maximum number of attempts.
'''
import random


def random_number(min:int,max:int,numero_tentativi:int):
    n=1
    numero_casuale=random.randint(min,max)
    tentativo=int(input("Prova ad indovinare: "))
    while n<=numero_tentativi:
        if tentativo>max or tentativo<min:
            print ("Non sei nel range!")
            tentativo=int(input("Scrivi un numero nel range: "))
        else:
            if tentativo==numero_casuale:
                print ("Hai vinto!")
                win=True
                break
            elif tentativo>numero_casuale:
                print ("Sbagliato! il numero corretto è più basso")
                if numero_tentativi==n:
                    win=False
                    break
                else:
                    n+=1
                    tentativo=int(input("Riprova: "))
            elif tentativo<numero_casuale:
                print ("Sbagliato! il numero corretto è più alto.")
                if numero_tentativi==n:
                    win=False
                    break
                else:
                    n+=1
                    tentativo=int(input("Riprova: "))
    if win!=True:
        print ("Hai perso!")

min=int(input("Inserisci valotre minimo nel range: "))
max=int(input("Inserisci valore massimo nel range: "))

while min>=max:
    print("Inserisci un range giusto")
    min=int(input("Inserisci valotre minimo nel range: "))
    max=int(input("Inserisci valore massimo nel range: "))


numero_tentativi=int(input("Inserisci numero di tentativi per cui vuoi indovinare: "))

random_number(min,max,numero_tentativi)

        
        

