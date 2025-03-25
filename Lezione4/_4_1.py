'''Create a function that takes a student's name and their scores in different subjects as input.
The function calculates the average score and prints the student's name, average, and a message 
indicating whether the student passed the exam (average >= 60) or failed.
Create a for loop to iterate over a list of students and scores, calling the function for each student.'''


def media_studente(studente:str,voti):
    n=0
    somma=0
    for voto in voti:
        somma=somma+voto
        n+=1


    media=somma/n
    print (f"La media dello studente {studente} è {media:.2f}")
    return media

def studente_ammesso(studente,media):
    if media>10 or media<0:
        print ("media non valida")
    elif media>6:
        print (f"Lo studente {studente} è stato ammesso")
    else:
        print (f"Lo studente {studente} non è stato ammesso")
    


studente=input(str("inserisci nome studente: "))
voti:list=[]
voto=int(input("Inserisci voto: "))
while voto!=0:
    if voto<0 or voto>10:
        print("Voto non valido")
        voto=int(input("Inserisci voto: "))
    else:
        voti.append(voto)
        voto=int(input("Inserisci voto: "))

    

media=media_studente(studente,voti)
studente_ammesso(studente,media)




        



               
                
                

    

