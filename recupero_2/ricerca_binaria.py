def ricerca_binaria(n:int,lista_o:list) ->bool:
    
    
    start=0
    end= len(lista_o)-1
    mid = (end+start)//2
    
    
    while n!=lista_o[mid]:
        if start>end:
            return False
        elif lista_o[mid]>n:
            end= mid -1
            mid = (end+start)//2
        elif lista_o[mid]<n:
            start = mid+1
            mid = (end+start)//2
    return True

list = [1, 3, 5, 7, 9]
print (ricerca_binaria(3, list ))
print (ricerca_binaria(-1, list)) 
print (ricerca_binaria(9, list))
print (ricerca_binaria(1, list))
        


                
            
            

        
        