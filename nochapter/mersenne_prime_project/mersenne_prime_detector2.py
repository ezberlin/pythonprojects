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
    
def isNumberPrime(n):
    n = str(n)
    dividers = 0
    n = int(n)
    if n == 1:
        return 0
    for i in range(1, int(n ** 0.5) + 1):
        if(n / i == int(n / i)):
            dividers = dividers + 1
            if dividers == 2:
                break
    if(dividers == 1):
        return 1
    else:
        return 0

mp_number = 0
for a in range(1,1024):
    if isNumberPrime(2**a-1):
        mp_number = mp_number + 1
        print(f"{mp_number}. mersenne: {2**a-1} (2^{a} - 1)")