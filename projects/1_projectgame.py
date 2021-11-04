import random

def gamewin(com, you):
    if com==you:
        return  None
    # Check for all possibilities when computer chose s
    elif com=="s":
        if you == "w":
            return False
        elif you=="g":
            return True

    # Check for all possibilities when computer chose w
    elif com == "w": 
        if you=="g":
            return False
        elif you == "s":
            return True

    # Check for all possibilities when computer chose g
    elif com == "g":
        if you=="s":
            return False
        elif you == "w":
            return True





print("com turn: sanke(s) water(w)  or gun(g)?")
rand = random.randint(1,3)

if rand ==1:
    com = "s"
elif rand ==2:
    coom = "w"
elif rand ==3:
    com = "g"

you =  raw_input("com turn: sanke(s) water(w)  or gun(g)?")

a = gamewin(com, you)

print("computer chose " + com)
print("you chose " + you)

if a == None:
    print("the game is a tie!")
elif a:
    print("you win!")
else:
    print("you lose!")