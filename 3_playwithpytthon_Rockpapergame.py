import random

from win32com.client import Dispatch


def gamewin(com, user):
    if com==user:
        return  None
    # Check for all possibilities when computer chose s
    elif com=="s":
        if user == "r":
            return False
        elif user=="p":
            return True

    # Check for all possibilities when computer chose w
    elif com == "p": 
        if user=="s":
            return False
        elif user == "r":
            return True

    # Check for all possibilities when computer chose g
    elif com == "r":
        if user=="p":
            return False
        elif user == "s":
            return True


speak =  Dispatch("SAPI.SpVoice")
speak.Speak("stone, paper, scissor")

print("choice your inpurt stone(s) paper(p) scissor(r)")
rand = random.randint(1,3)

if rand == 1:
    com = "s"
elif rand == 2:
    com =  "p"
elif rand == 3:
    com  = "r"

user = raw_input("choice your inpurt stone(s) paper(p) scissor(r) ")


a = gamewin(com, user)

b = "you choice " + user
print(b)
speak =  Dispatch("SAPI.SpVoice")
speak.Speak(b)
d = "computer choice " + com
print(d)
speak =  Dispatch("SAPI.SpVoice") 
speak.Speak(d)


e = "the game is a tie!"
f ="you win!"
d = "you lose!"
if a == None:
    print(e)
    speak =  Dispatch("SAPI.SpVoice")
    speak.Speak(e)
elif a:
    print(f)
    speak =  Dispatch("SAPI.SpVoice")
    speak.Speak(f)
else:
    print(d)
    speak =  Dispatch("SAPI.SpVoice")
    speak.Speak(d)
