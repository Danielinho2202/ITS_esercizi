def count_isolated(lista:list) -> int:
    counter=0
    count=0
    for number in lista:
        if number== lista[number-1] or number== lista[number+1]:
            counter+=1
        else:
            count+=1
           
    
    return (count)





print(count_isolated([1, 2, 2, 3, 3, 3, 4]))


print(count_isolated([1, 2, 3, 4, 5]))