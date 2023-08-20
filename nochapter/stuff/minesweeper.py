import random, os
minen = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
aufgedeckt = minen 

for reihe in range(0, 7):
    for spalte in range(0, 7):
        if random.random() > 0.9:
            minen[reihe][spalte] = 1
            
def benachbart(r, s):
    nachbarn = []
    if r<7:
        nachbarn.append([r+1, s])
        if s<7:
            nachbarn.append([r+1, s+1])
        if s>0:
            nachbarn.append([r+1, s-1])
    
    if r>0:
        nachbarn.append([r-1, s])
        if s<7:
            nachbarn.append([r-1, s+1])
        if s>0:
            nachbarn.append([r-1, s-1])
    
    if s<7:
        nachbarn.append([r, s+1])
        
    if s>0:
        nachbarn.append([r, s-1])
        
    return nachbarn

print(benachbart(5, 5))
        

        
        