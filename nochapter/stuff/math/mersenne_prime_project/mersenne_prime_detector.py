mp_number = 0
for n in range(2,100_000_001):
    if ez.isNumberMersenne(n) and ez.isNumberPrime(n):
        mp_number = mp_number + 1
        print(f"{mp_number}: {n}")