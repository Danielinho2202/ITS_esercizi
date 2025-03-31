import random

def password(lenght:int,tipi_carattere:str):
    
    minuscole:list=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o",
               "p","q","r","s","t","u","v","w","x","y","z"]
    maiuscole:list=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O",
                    "P","Q","R","S","T","U","V","W","X","Y","Z"]
    numeri:list=["1","2","3","4","5","6","7","8","9","0"]
    simboli:list=["!","£","$","%","&","/","(",")","?","@","#","*","_","-",":",";"]
    
    
    if tipi_carattere=="minuscolo":
        password= random.choices(minuscole, k=lenght)
        print ("".join(password))
    elif tipi_carattere=="maiuscolo":
        password= random.choices(maiuscole, k=lenght)
        print ("".join(password))
    elif tipi_carattere=="numero":
        password= random.choices(numeri,k=lenght)
        print ("".join(password))
    elif tipi_carattere=="simbolo":
        password= random.choices(simboli,k=lenght)
        print ("".join(password))
    else:
        print ("carattere non riconosciuto")
        tipo_carattere="non riconosciuto"
        while tipo_carattere=="non riconosciuto":
            tipi_carattere=str(input("Scegli il tipo di carattere: 'maiuscolo', 'minuscolo', 'numero', 'simbolo'. "))
            if tipi_carattere=="minuscolo":
                password= random.choices(minuscole, k=lenght)
                print ("".join(password))
                break
            elif tipi_carattere=="maiuscolo":
                password= random.choices(maiuscole, k=lenght)
                print ("".join(password))
                break
            elif tipi_carattere=="numero":
                password= random.choices(numeri,k=lenght)
                print ("".join(password))
                break
            elif tipi_carattere=="simbolo":
                password= random.choices(simboli,k=lenght)
                print ("".join(password))
                break
            else:
                print ("carattere non riconosciuto")
                tipo_carattere="non riconosciuto"

tipo_carattere=str(input("Scegli il tipo di carattere: 'maiuscolo', 'minuscolo', 'numero', 'simbolo'. "))
numero_caratteri=int(input("secgli numero di caratteri: "))

password(numero_caratteri,tipo_carattere)

    
