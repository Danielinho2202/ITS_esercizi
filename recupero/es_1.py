def tup_in_dict(lista:list[tuple[int,int]]) -> dict:
    new_dict:dict={}
    for tuple in lista:
        if tuple[0] in new_dict.keys():
            new_dict[tuple[0]] += tuple[1]
        else:
            new_dict[tuple[0]] = tuple[1]

    return new_dict


lista = [('a', 1), ('b', 2), ('a', 3), ('c', 4), ('b', 5)]
dizionario_risultante = tup_in_dict(lista)
print(dizionario_risultante) 
