def somma_matrici_primary(lista:list[list]):
    index=0
    somma=0
    for lis in lista:
        somma=somma+lis[index]
        index+=1
    return somma
mat1 = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
print (somma_matrici_primary(mat1))


def somma_matrici_secondaria(lista:list[list]):
    index=len(lista)
    somma=0
    for lis in lista:
        somma=somma+lis[index]
        index-=1
    return somma
mat1 = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]
print (somma_matrici_primary(mat1)) 