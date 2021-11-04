import random

rand = random.randint(1,100)


user = None
guesses = 0


while(user != rand):
    user  = int(input("enter your gusess : "))
    guesses += 1
    if(user==rand):
        print("you guessed it right!")
    else:
        if(user>rand):
            print("you guessed it wrong! enter a smaller number")
        else:
            print("you guessed it wrong! enter a larger number")

print("you guessed the  number in " + str(guesses) +  " guesses")

with open("D:\pyton file\projects\hislog.txt", "r") as f:
    history = int(f.read())

if(guesses<history):
    with open("D:\pyton file\projects\hislog.txt", "w") as f:
        write = f.write(str(guesses))
    print("you have just broken the high score")
