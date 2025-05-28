import time

def bubble_sort(lista:list[int]) -> list[int]:

    for i in range (len(lista)):
        ordered=True

        for j in range (i + 1,len(lista)):
            minimo=lista[i]

            if minimo>=lista[j]:
                minimo=lista[j]
                lista[i],lista[j]=lista[j],lista[i]
                ordered=False
        if ordered:
            return lista

    return lista


start = time.time()
print(bubble_sort([3,10,5,2,12,29]*5000))
print(time.time()- start)