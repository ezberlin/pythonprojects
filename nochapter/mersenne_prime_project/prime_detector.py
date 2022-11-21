def isNumberPrime(n):
    import math
    n = str(n)
    dividers = 0 #dividers without 1
    if n.isdigit():
        n = int(n)
        if n == 1:
            return 0
        for i in range(1, int(math.sqrt(n) + 1)):
            if(n / i == int(n / i)):
                dividers = dividers + 1
                if dividers == 2:
                    break
        if(dividers == 1):
            return 1
    else:
        return 0
        print("no integer as n")
        
        
    