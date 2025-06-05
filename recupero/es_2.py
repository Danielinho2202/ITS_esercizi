def sep_num(lista:list) -> dict:
    n_dict={"positivo":[],"negativo":[]}
    for num in lista:
        if num<0:
            n_dict["negativo"].append(num)
        else:
            n_dict["positivo"].append(num)

    return n_dict

lista:list=[1,5,4,3,7,8,-9,-5,-4,-3]
print (sep_num(lista))
