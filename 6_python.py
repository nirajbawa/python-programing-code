# practice set

# 1. write a program to find greatest four number entered by the user


# num1 = int(input("inter number 1 : "))
# num2= int(input("inter number 2 : "))
# num3= int(input("inter number 3 : "))
# num4= int(input("inter number 4 : "))

# if(num1>num2):
#     f1 = num1
# else:
#     f1 = num4

# if(num2>num3):
#     f2 = num2
# else:
#     f2 = num3

# if(f1>f2):
#     print(f1,"is greatest")
# else:
#     print(f2,"is greatest")

# 2. make program check mark of student pass or fail


# sub1 = int(input("enter your 1 sub mark"))
# sub2 = int(input("enter your 2 sub mark"))
# sub3 = int(input("enter your 3 sub mark"))


# if(sub1<33 or sub2<33 or sub<33):
#     print("you are faill  because you have less then 33% in one of the subjects ")

# elif (sub1+sub2+sub3)/3 <40:
#     print("you are fail due to total percentage  less then 40")
# else:
#     print("congatulations! you are pass the test ")



# 3.  a spam comment is definted as a teat containsing following keywords

# user_input = raw_input("inter input : \n")

# if("subscribe my channel" in user_input):
#     spam = True
# elif ("you are non-sense" in  user_input):
#     spam = True
# elif("hello" in user_input):
#     spam =  True
# elif("this is my name" in user_input):
#     spam = True
# else:
#     spam = False

# if(spam is  True):
#     print("this is spam")
# else:
#     print("this is not spam")


# 4. write a program to find whether a given username contains less then 10  chercters or not


# name =  raw_input("inter your name  : \n")

# if(len(name)<10):
#     print("user name contains chercters is less then 10")
# else:
#     print("user name contains chercters is greter then 10")

# 5. write a program which  finnde out whether a given name is present in a list or  not

# lists = ["niraj","shreyas","ram"]

# user =  raw_input("inter name here : \n")

# if(user in lists):
#     print("name is get")
# else:
#     print("name is not get")

# 6. write a program to  calculate the grade of a  student from his marks from  the following scheme 

# mark = int(input("inter your mark : \n"))

# if(mark>90):
#     grade = "ex"
# elif (mark>80):
#     grade = "a"
# elif (mark>70):
#     grade = "b"
# elif (mark>60):
#     grade = "c"
# elif (mark>50):
#     grade = "d"
# else:
#     grade = "f"


# print("your mark grade is " + grade)


# 7. write a program  to findd  out  wheter a given post is talking about "harry"  or not


post =  "hello haRRry what are you doing"

find = "harry"

if("harry" in find):
    print("talk about harry")
else:
    print("not talk about harry")


