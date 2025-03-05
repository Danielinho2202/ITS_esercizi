
'''somma=0
for i in range (1 , 11):
    somma=somma+i

print (f"la somma dei numeri da 1 a 10 è: {somma}")

somma=0
for i in range (20 , 38):
    somma=somma+i

print (f"la somma dei numeri da 1 a 10 è: {somma}")

somma=0
for i in range (35 , 50):
    somma=somma+i

print (f"la somma dei numeri da 1 a 10 è: {somma}")'''

#con funzione

'''def somma(a:int,b:int):
    somma=0
    for i in range (a, b+1):
        somma=somma+i
    
    return (somma)

mysum_in_range=somma(35,49)
print (f"somma da 1 a 10 è: {somma(1,10)}")
print (f"somma da 1 a 10 è: {somma(20,37)}")
print (f"somma da 1 a 10 è: {somma(35,49)}")
print (f"somma da 1 a 10 è: {mysum_in_range}")'''


    
#un altro esercizio
'''def sottrazione(a:int,b:int):
    sottrazione=a-b

    return (sottrazione)

print (sottrazione(3,2))
print (sottrazione(263,53737))
print (sottrazione(-20,-20))'''

#esercizio 1
'''def check_value(n:int):
    if n>5:
        return (f"{n} è maggiore di 5")
    elif n<5:
        return (f"{n} è minore di 5")
    else:
        return (f"{n} è uguale a 5")

print (check_value (1))
print (check_value(13))
print (check_value(5))'''


# esercizio 2

'''def check_lenght(string:str):
    if len(string)>10:
        return (f"{string} ha più di 10 caratteri")
    elif len(string)<10:
        return (f"{string} ha meno di 10 caratteri")
    else:
        return (f"{string} ha esattamente di 10 caratteri")
    
string1=check_lenght("ciao")
string2=check_lenght("ciao come stai?")
string3=check_lenght("characters")

print(string1)
print(string2)
print(string3)'''

#esercizio 3

'''def print_numbers (num_list):
    for num in (num_list):
        print (num)

lista_prova=[1,6,4,6,5]
(print_numbers(lista_prova))'''

#esercizio 4

'''def check_each(number_list):
    for number in number_list:
        if number>5:
            print (f"{number} è maggiore di 5")
        elif number<5:
            print (f"{number} è minore di 5")
        else:
            print (f"{number} è uguale a 5")

my_list=[8,2,4,5,0]

(check_each(my_list))'''

#esercizio 5

def add_one(n:int):
    n+=1
    return n

def add_one_to_list(numbers_list):
    new_list=[]
    for number in numbers_list:
        new_number=add_one(number)
        new_list.append(new_number)
    print (new_list)

my_list=[4,5,6,7]
add_one_to_list(my_list)





