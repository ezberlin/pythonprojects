import json

def getStoredBoard():
    boardsave = "boardsave.json"
    try:
        with open(boardsave) as f:
            board = json.load(f)
    except FileNotFoundError:
        return None
    else:
        print("opened!")
        return board
def enterNewBoard():
    board = []
    for num in range(1,65):
        while len(board) != num:
            cur = input(f"OK. Please enter {num}. number: ")
            while cur == str(cur):
                try:
                    cur = int(cur)
                except ValueError:
                    cur = input("Enter a number: ")
            while cur > 9 or cur < 1 and cur == str(cur):                
                while cur > 9 or cur < 1:
                    cur = input("Enter a number > 0 and < 10: ")
                    while cur == str(cur):
                        try:
                            cur = int(cur)
                        except ValueError:
                            cur = input("Enter a number: ")
                while cur == str(cur):
                    try:
                        cur = int(cur)
                    except ValueError:
                        cur = input("Enter a number: ")
            num = num + 1    
            
                
        
    boardsave = "boardsave.json"
    with open(boardsave, "w") as f:
        json.dump(board, f)
    print("saved!")        
    
    return board

b = input("Welcome to MATCHTRIO! Enter o to open board, and n to create new! ")
chosen = 0
while not chosen:
    if b == "o":
        boardy = getStoredBoard()
        chosen = 1
    elif b == "n":
        boardy = enterNewBoard()
        chosen = 1
    else:
        b = input("Choose to enter o to open a board, or n to create a new! ")

answer = 0
while not answer == "N":

    n = input("Enter the number I should search for you: ")
    while n == str(n):
        try:
            n = int(n)
        except ValueError:
            n = input("Enter an integer I should search for you: ")
    for t in range (1, 65):
        element = boardy[t - 1]
        element2 = 0
        element3 = 0
        #up
        if t >= 17:
            t2 = t - 8
            t3 = t - 16
            element2 = boardy[t2 - 1]
            element3 = boardy[t3 - 1]
            trio = element * element2 + element3
            if n == trio:
                print(f"Found on index {t} times index {t2} plus index {t3}!")
                break
            trio = element * element2 - element3
            if n == trio:
                print(f"Found on index {t} times index {t2} minus index {t3}!")
                break
        
        #up right
        if t >= 17 and (t - 1) % 8 <= 5:
            t2 = t - 7
            t3 = t - 14
            element2 = boardy[t2 - 1]
            element3 = boardy[t3 - 1]
            trio = element * element2 + element3
            if n == trio:
                print(f"Found on index {t} times index {t2} plus index {t3}!")
                break
            trio = element * element2 - element3
            if n == trio:
                print(f"Found on index {t} times index {t2} minus index {t3}!")
                break
        #right
        if (t - 1) % 8 <= 5:
            t2 = t + 1
            t3 = t + 2
            element2 = boardy[t2 - 1]
            element3 = boardy[t3 - 1]
            trio = element * element2 + element3
            if n == trio:
                print(f"Found on index {t} times index {t2} plus index {t3}!")
                break
            trio = element * element2 - element3
            if n == trio:
                print(f"Found on index {t} times index {t2} minus index {t3}!")
                break
            
        #down right
        if t <= 47 and (t - 1) % 8 <= 5:
            t2 = t + 9
            t3 = t + 18
            element2 = boardy[t2 - 1]
            element3 = boardy[t3 - 1]
            trio = element * element2 + element3
            if n == trio:
                print(f"Found on index {t} times index {t2} plus index {t3}!")
                break
            trio = element * element2 - element3
            if n == trio:
                print(f"Found on index {t} times index {t2} minus index {t3}!")
                break
            
        #down
        if t <= 47:
            t2 = t + 8
            t3 = t + 16
            element2 = boardy[t2 - 1]
            element3 = boardy[t3 - 1]
            trio = element * element2 + element3
            if n == trio:
                print(f"Found on index {t} times index {t2} plus index {t3}!")
                break
            trio = element * element2 - element3
            if n == trio:
                print(f"Found on index {t} times index {t2} minus index {t3}!")
                break
            
        #down left
        if t <= 47 and (t - 1) % 8 >= 2:
            t2 = t + 7
            t3 = t + 14
            element2 = boardy[t2 - 1]
            element3 = boardy[t3 - 1]
            trio = element * element2 + element3
            if n == trio:
                print(f"Found on index {t} times index {t2} plus index {t3}!")
                break
            trio = element * element2 - element3
            if n == trio:
                print(f"Found on index {t} times index {t2} minus index {t3}!")
                break
            
        #left
        if (t - 1) % 8 >= 2:
            t2 = t - 1
            t3 = t - 2
            element2 = boardy[t2 - 1]
            element3 = boardy[t3 - 1]
            trio = element * element2 + element3
            if n == trio:
                print(f"Found on index {t} times index {t2} plus index {t3}!")
                break
            trio = element * element2 - element3
            if n == trio:
                print(f"Found on index {t} times index {t2} minus index {t3}!")
                break
            
        #up left
        if t >= 17 and (t - 1) % 8 >= 2:
            t2 = t - 9
            t3 = t - 18
            element2 = boardy[t2 - 1]
            element3 = boardy[t3 - 1]
            trio = element * element2 + element3
            if n == trio:
                print(f"Found on index {t} times index {t2} plus index {t3}!")
                break
            trio = element * element2 - element3
            if n == trio:
                print(f"Found on index {t} times index {t2} minus index {t3}!")
                break
            
        #up
        if t >= 17:
            t2 = t - 8
            t3 = t - 16
            element2 = boardy[t2 - 1]
            element3 = boardy[t3 - 1]
            trio = element * element2 + element3
            if n == trio:
                print(f"Found on index {t} times index {t2} plus index {t3}!")
                break
            trio = element * element2 - element3
            if n == trio:
                print(f"Found on index {t} times index {t2} minus index {t3}!")
                break
    print("done!")
    answer = 0
    while(answer != "N" and answer != "y"):
        answer = input("Would you like to retry? (y/N) ")
        answer = str(answer)







  

    


            
    
    
    
    
        
        


    
