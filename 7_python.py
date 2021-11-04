# # write a program  to print 1 to 50  using  a while loop
# i  =  0
# while i<=50:
#     print(str(i))
#     i =  i+1

# # write a program to print the content of a list using while executed

# a =  ["niraj", "shreyash", "mehul", "mrudul", "kalpesh"]

# b  =  0

# while b<len(a):
#     print(a[b])
#     b = b+1


# for i in range(1, 10, 2):
#     print(i)
# else :
#     print("this is inside else of for")

# for i in range(1, 10):
#     if i%2!= 0:
#         print(i)

# pracitce set 

# 1. write a program  to print multipication  table of a given number using for loop

# num  = int(input("enter the number  : "))

# for i in range(1, 20):
#     # print(str(num) + "x" + str(i) +"=" + str(i*num))
#        print(f"{num}x{i}={num*i}")


# 2. write a program  to gsset all the person names stored in a list l1 and which stsasts with 5

# l1 = ["harry", "soham", "sachin", "rahul"]

# for name in l1 :
#     if name.startswith("s"):
#         print("hello " + name)


# 3. attemp  problem 1 using while loop

# u = int(input("inter the number "))

# i = 0

# while i<10:
#     i = i+1
#     print(str(u)+"x"+str(i)+"="+str(u*i))
    
# 4. write a program to find whether a given number is prim or not

# i = int(input("inter number"))

# for i in range(2, i):
    

# 5. write a program to  find the sum to first n natrueal  number for loop

# user_input = int(input("inter number : "))

# prime =  True

# for a in range(2,  user_input):
#     if(user_input%i==0):
#         prime =  False
#         break
# if prime : 
#     print("this number is prime")
# else:
#     print("this number is not prime")


# pr


# num =  int(input("inter number"))

# f  = 0

# for i  in range(1,num+1):
#     f = f+i
    
# print(f)    

# 6. write a program  to clculate the factorial of a given number using for loop


# num =  int(input("inter number"))

# f  = 1

# for i  in range(1,num+1):
#     f= f*i
    
# print(f)    


# 7. write a program  to print the following star pattern



# for i in range(3):
#     print("*"*(i+1))

# 8. write a progarm to  print the following stas pattern
# import sys

# n =  4
# for i in range(4):
#     print(" "*(n-i-1))
#     print("*"*(2*i+1))
#     print(" "*(n-i-1))

# 9. write a program to print the following star pattern 

# n = 3
# for i in range(3):
#     print(" *  * "*(1))
#     for i in range(1):
#         print(""*(2*i-1))

# 8. 

num  = int(input("enter the number  : "))
i = 1
li=[0,10,9,8,7,6,5,4,3,2,1]

while i<len(li):
    print(str(num)+"x"+str(li[i])+"="+str(num*li[i]))
     # print(str(num) + "x" + str(i) +"="+ str(i*num))
    i  =  i+1
    

    