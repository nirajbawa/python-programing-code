# def func(name):
#     name.capitalize()
#     print("good day, "+name)

# func(raw_input("Inter Your Name "))

# def su(num1, num2):
#     return num1+num2 

# s = su(int(input("inter num 1st")), int(input("inter number 2nd")))

# print(s)



# practice set 

# 1. write a program using function to find greatest of three numbers

# def greatest(num1,num2,num3):
#     if (num1>num2):
#         if(num1>num3):
#             return num1
#         else:
#             return num3
#     else:
#         if(num2>num3):
#             return num1
#         else:
#             return num3

# s  = greatest(32,21,50)

# print(s)

# 2. write a python using function to covert celsuses of fehreheit   


# def f(cel):
#     return  (cel *(9/5)) + 32

# value = f(30)

# print("fahreheit temperature is "+ str(value))


# 3. how  do you prevent a python pprint function  to  print  a new line at the end


# print("hello\n")
# print("how\n")
# print("are\n")
# print("you\n")


# 4. write a recusive function to calculate the sum of first n natural numbers

# def fac(num):
#     if num ==1 or num==0:
#         return 1
#     return num+fac(num-1)    

# n  = fac(2)

# print(n)

 
# 5. write a python function to print firstv n lines of the following pattern


# n =3
# for  i  in  range(n):
#     print("*"*(n-i))


# 6. write a python function which converts inches to cms


# def intocm(inc):
#     return inc*2.54

# a = intocm(5)
# print(a)


# 7.  write a python function  to remove a given word from  a list and step it at the same fime

# def remove(string, word, name):
#     new = string.replace(word, name)
#     return new.strip()



# this =  "   harry is a good   "
# m = remove(this, "harry", "niraj")
# print(m)

# 8. write a python function to print muliplivstion table of given number

def  mul(num):
    for i in range(1,10+1):
        print(str(num)+"x"+str(i)+"="+str(num*i))

a = mul(int(input("inter number : ")))