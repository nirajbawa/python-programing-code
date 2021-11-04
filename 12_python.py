while(True):
    print("press q to quit ")
    user = raw_input("enter a number ")
    
    if user  ==  "q":
        break

   

    try :
        print("trying....")

        user= int(user)

        if user>6:
            print("greater")
        else:
            print("smaller")
    except Exception as e :  
    
        print(e)

print("thanks  for playing this  game")

# pratice set 

# 1. 

# def readFile(filename):
#     try:
#         with open(filename, "r") as f :
#             print(f.read())
#     except FileNotFoundError :
#              print(filename) 

# readFile("D:\\pyton file\\1.txt")
# readFile("D:\\pyton file\\2.txt")
# readFile("3.txt")

# 2.

# l = [1,2,3,4,5,6,7,8,9,10]

# for index, item in enumerate(l):
#     if index == 2 or index==4 or index==6:
#         print(index , item)

#         print("the " + str(index) + "th element is " + str(item))

# 3.

# num = int(input("enter the number "))

# table = [num*i for i in range(1, 11)]
# print(table)

# 4. 


# a = int(input("inter number a  : "))
# b = int(input("inter number b  : "))


# try:
#     print(a/b)
# except:
#     print("infinite")


# 5.

num = int(input("enter the number "))

table = [num*i for i in range(1, 11)]
print(str(table))

with open("table.txt", "a") as f:
    f.write(str(table))
    f.write("\n")