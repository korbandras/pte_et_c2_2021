import random
winner=False
while not winner:
    try:
        player=int(input("Melyik? 1 - rock, 2 - paper, 3 - scisors\n"))
        bot=random.randint(1,3)
        if player==bot:
            print("Draw")
        elif (player==1 and bot==3) or (player==2 and bot==1) or (player==3 and bot==2):
            print("Player wins")
            winner=True
        elif (player==1 and bot==2) or (player==2 and bot==3) or (player==3 and bot==1):
            print("Computer wins")
            winner=True
        else:
            print("moron")
    except:
        print("moron")