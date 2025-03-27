'''def recursive_Countdown(n:int) -> None:
    if n<0:
        print ("errore")
    elif n==0:
        print (0)
    else:
        print (n)
        recursive_Countdown(n-1)

recursive_Countdown (-5)
recursive_Countdown '''


'''def recursiveSum(n:int) -> int:
    if n<0:
        print ("errore")
        return None
    if n==0:
        return 0
    else:
        return int(n+recursiveSum(n-1))
    


print (recursiveSum(5))'''


def sum_in_range(a,b):
    if a>b:
        temp=a
        a=b
        b=temp

    if a==b:
        return int(b)
        #return int(a)
    else:                                   #vanno bene entrambi i modi
        return (a+sum_in_range(a+1,b))
        # return (b+sum_in_range(a,b-1))

print (sum_in_range (1,5))
