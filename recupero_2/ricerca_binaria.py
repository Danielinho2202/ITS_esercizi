def ricerca_binaria(n:int,lista_o:list) ->bool:
    
    
    start=0
    end= len(lista_o)-1
    mid = (end+start)//2
    
    
    while n!=lista_o[mid]:
        if start>end:
            return False
        if lista_o[mid]==n:
            return True
        elif lista_o[mid]<n:
            end= mid -1
            mid = (end+start)//2
        elif lista_o[mid]>n:
            start = mid+1
            mid = (end+start)//2

list = [1, 3, 5, 7, 9] 
print (ricerca_binaria(list, 3)) # => 1 
print (ricerca_binaria(list, -1)) # => None 

        


                
            
            

        
        