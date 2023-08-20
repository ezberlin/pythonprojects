import random
players = input("Welcome to High Scored! How many players do we have? ")
guesses = []
for i in range(0, int(players)):
    guesses.append(int(input(f"Which number does Player {i+1} guess? ")))
    
high = 0
highcount = 0

print(guesses)
    
for i in range(1, 11):
    newrandom = random.randrange(1, 101)
    if newrandom > high:
        high = newrandom
        highcount = highcount + 1
        input(f"We're now in round {i}. Our new random number is {newrandom}. This is now our highscore. We just had {highcount} highscores.")
    else:
        input(f"We're now in round {i}. Our new random number is {newrandom}. We just had {highcount} highscores.")
        
if (highcount in guesses):
    print(f"Player {guesses.index(highcount) + 1} guessed the number of highscores right!")
else:
    print("No one guessed the number of highscores right!")
    
    

    