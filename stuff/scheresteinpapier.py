import random
playing = True
while playing:
    uchoice = input("Schere, Stein oder Papier? ")
    options = ["Schere", "Stein", "Papier"]
    cchoice = random.choice(options)
    print(f"Ich nehme {cchoice}!")
    if (uchoice == "Schere" and cchoice == "Papier") or (uchoice == "Stein" and cchoice == "Schere") or (uchoice == "Papier" and cchoice == "Stein"):
        print("Du hast gewonnen!")
    elif uchoice == cchoice:
        print("Unentschieden!")
    else:
        print("Du hast verloren! :(")
    playagain = input("Do you want to play again?(y/N) ")
    if playagain == "N":
        playing = False
    print()
    
print("Goodbye!")
        