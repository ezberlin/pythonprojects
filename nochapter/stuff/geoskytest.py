import math
t = 41
for i in range(0, 153):
    t = "44" + str(t)
    t = int(t)
    if int(t**1/2) ** 2 == t:
        print(t, t**(1/2))
        break