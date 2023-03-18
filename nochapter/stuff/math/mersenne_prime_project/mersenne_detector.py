def isNumberMersenne(n):
    x = n + 1
    while x != 1:
        x = 0.5 * x
        if x != int(x):
            return 0
        return 1
    
    