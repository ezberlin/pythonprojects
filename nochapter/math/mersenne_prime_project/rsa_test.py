import secrets as sc

def isNumberPrime(n): #check if number is prime
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
        
def findPrime(n): #find the nth prime
    testnum = 2
    for i in range(0, n):
        while not isNumberPrime(testnum):
            testnum = testnum + 1
        testnum = testnum + 1
    testnum = testnum - 1
    return(testnum)
            
def findInvert(a, n):#finds solution to (a times d) is congruent to 1 modulo n
    testd = 1

    while True:
        if (testd * a - 1) % n == 0:
            break
        else:
            testd = testd + 1
        
    return testd

def generateKey():
    p = 0
    q = 0
    while p == q:
        p = findPrime(sc.choice(range(1, 100)))
        q = findPrime(sc.choice(range(1, 100)))
    n = p * q
    h = (p - 1) * (q - 1)
    e = h - 1
    d = findInvert(e, h)
    print(f"public key: \n e = {e} \n n = {n}")
    print(f"private key: \n p = {p} \n q = {q} \n d = {d}")

def lockCharacter(c, e, n):
    int_character = ord(c)
    locked = (int_character ** e) % n
    return locked

def unlockCharacter(l, d, n):
    return chr((l ** d) % n)

def lockString(string, e, n):
    characters = [*string]
    locked_string = ""
    for character in characters:
        locked_string = locked_string + str(lockCharacter(character, e, n)) + "-"
    return locked_string

def unlockString(lstring, d, n):
    unlocked_string = ""
    check = ""
    characternum = 0
    while characternum <= len(lstring):
        while lstring[characternum - 1] != "-":
            check = check + lstring[characternum]
            characternum = characternum + 1
        check = int(check)
        unlocked_string = unlocked_string + unlockCharacter(check, d, n) #error, need to fix
        check = ""
        characternum = characternum + 1
    return unlocked_string

unlockString("11125-5327-11129-506-11129-", 10947, 11233)
        
        
            
    






        
        
        
    
    
 