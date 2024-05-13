def collatz(num):
    history = []
    while num != 1:
        history.append(num)
        if num % 2 == 0:
            num = int(num / 2)
        else:
            num = 3 * num + 1
    history.append(1)
    return history

print("Die History ist: " + str(collatz(7)))
