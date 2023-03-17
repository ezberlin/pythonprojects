def findInvert(a, n):#finds solution to (a times d) is congruent to 1 modulo n
    testd = 1

    while True:
        if (testd * a - 1) % n == 0:
            break
        else:
            testd = testd + 1
        
    return testd