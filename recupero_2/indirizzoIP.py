def is_valid_ipv4(address:str) ->bool:
    lista= address.split(".")
    counter=0
    for el in lista:
        counter+=1
        if len(el)>3:
            return False
        elif not el.isdigit():
            return False
        elif int(el)>255:
            return False

    if counter!=4:
        return False
    else:
        return True




print(is_valid_ipv4("192.168.0.1")) # True
print(is_valid_ipv4("255.255.255.255")) # True
print(is_valid_ipv4("256.100.10.1")) # False (256 è fuori range)
print(is_valid_ipv4("192.168.1")) # False (solo 3 parti)
print(is_valid_ipv4("192.168.1.a")) # False (parte non numerica)