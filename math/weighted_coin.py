import random, math

def weighMyCoin(weighting, n):
    level = 0.5
    heads = 0
    for i in range(0, weighting):
        heads = 0

        for j in range(0, n):
            ran = random.random()
            if ran < level:
                heads += 1
        
        level = heads / n
    return level

results = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for k in range(0, 100):
    results[math.floor(weighMyCoin(1000, 10000) * 10)] += 1
print("------")
print(results)
print("------")