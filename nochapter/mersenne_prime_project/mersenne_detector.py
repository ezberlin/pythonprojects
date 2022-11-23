def isNumberMersenne(n):
    x = n + 1
    while x != 1:
        x = 0.5*x
        if x != int(x):
            break
    if x == 1:
        return 1
    else:
        return 0
    