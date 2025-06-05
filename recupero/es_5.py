def mult(lista:list, threshold:int):
    prodotto=1
    for num in lista:
        if num < threshold:
            prodotto*=num
    return prodotto


lista=[1,10,6,4]
threshold=9
print(mult(lista,threshold))