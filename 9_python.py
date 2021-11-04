# f =  open("D:\pyton file\demo.txt", "r")
# r =  f.read()
# print(r)
# c = f.close()

# f =  open("D:\pyton file\demo.txt", "r")
# r =  f.read(5)
# print(r)
# c = f.close()

# f =  open("D:\pyton file\demo.txt", "rt")
# r =  f.readline()# read line  1st
# print(r)
# r =  f.readline()# read line  2st
# print(r)
# r =  f.readline()# read line  3st
# print(r)
# c = f.close()




# f = open("niraj.txt", "w")
# write = f.write("hello i am niraj, good morning")
# f.close


# f = open("niraj.txt", "a")
# write = f.write(" byy")
# f.close


# f = open("D:\pyton file\demo.txt", "r")
# write = f.write("nothing is here")
# f.close


# with open("D:\pyton file\demo.txt", "r") as f:
#     a = f.read()
# print(a)

# pracitce  set

# 1. 

# f = open("D:\\pyton file\\twinkle.txt", "r")
# read = f.read()

# if raw_input('inter the search ')  in  read:
#     print("Twinkle in read.txt")
# else:
#     print("Twinkle is not in read.txt")


# print(read)
# f.close()

# 2

# def game():
#     return 45

# with open("D:\\pyton file\\scroce.txt", "r")  as file:
#     read =  file.read()

# if  read== "":
#     with open("D:\\pyton file\\scroce.txt","w") as f:
#         write = f.write(str(game()))
#     print("your  scroce is added")

# elif int(read)<game():
#     with open("D:\\pyton file\\scroce.txt", "w") as o:
#          o.write(str(game()))
#     print("your scroce is add")

# else:
#     print("your scroce is small")
    
    
# 3.

# for i in range(2,20+1):
#     with open("D:\\pyton file\\tables\\multiipliction table"+str(i)+".txt", "w")  as f:
#          for j in  range(1,10+1):
#              f.write(str(i)+"x"+str(j)+"="+str(i*j)+"\n")

# 4.

# with open("D:\pyton file\demo.txt") as f:
#      read = f.read()
 
# read = read.replace("donkey", "#")

# with open("D:\pyton file\demo.txt", "w") as f:
#     read = f.write(read)


# 5. 

# lis = ["mote","noob","pagal","yeda"]


# with open("D:\pyton file\demo.txt") as f:
#      read = f.read()
 
# for liS in lis:
#      with open("D:\pyton file\demo.txt", "w") as f:
#          read =  read.replace(liS, "#")
#          f.write(read)

# 6. 


# with open("D:\pyton file\log.txt",  "r") as f:
#      read = f.read()

# if  "python" in  read.lower() :
#      print("yes")

# else:
#      print("no") 


# 7.

# read = True
# i =  1

# with open("D:\pyton file\log.txt",  "r") as f:

#      while read :
          
#           read = f.readline()

#           if  "python" in  read.lower() :
#                print(read)
#                print("yes")
#                print(i)
#           i += 1

# 8. 

# with open("D:\pyton file\demo.txt",  "r") as file:
#      read =  file.read()

# with open("copy.txt", "w") as file:
#      file.write(read)

# 9.


# file1 = "D:\pyton file\demo.txt"
# file2 = "D:\pyton file\copy.txt"

# with open(file1,"r") as f:
#      read1 = f.read()
# with open(file2, "r") as f:
#      read2 = f.read()

# if read1 == read2 :
#      print("is equal")
# else:
#      print("not equal")

# 10.

# f = "D:\\pyton file\\niraj.txt"

# with open(f, "w") as fi:
#      fi.write("")


# 11.

oldFile= "D:\pyton file\sample.txt"
newFile = "renamed_by_python_.txt"

with open(oldFile,"r") as f:
     read = f.read()

with open(newFile, "w") as f:
     f.write(read)

import os

os.remove(oldFile)
