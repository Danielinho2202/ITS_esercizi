'''def printlistbackwards(lista:list):
    new_list=[]
    for i in range(len(lista)-1,-1,-1):
        new_list.append(lista[i])
    return new_list'''

lista1= [1, 2, 3, 4, 5]



def printlistbackwards(lista):
    if not lista:
        return 
    else:
        print(lista[-1])
        printlistbackwards(lista[:-1])
    
printlistbackwards(lista1)