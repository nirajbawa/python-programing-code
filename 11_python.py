# # 1.


# class c2dvec :
#     def __init__(self, i, j):
#         self.icap = i
#         self.jcap = j

#     def __str__(self):
#         return str(self.icap) + str(self.jcap)

# class c3dvec(c2dvec):
#     def __init__(self, i, j, k):
     
#         self.kcap = k 
    
#     def __str__(self):
#         return str(self.icap) + str(self.jcap) + str(self.kcap)

# v2d = c2dvec(1, 3)
# v3d = c3dvec(1, 9, 7)
# print(v2d)
# print(v3d)

#2. 

# class animals :
#     animaltype = "mammal"

# class pets :
#     color = "white"

# class dog:
#     @staticmethod
#     def bark():
#         print("bow bow!")

# d = dog()
# d.bark()

# 3.

# class employee:
#     salary = 1000
#     increment = 1.5
#     @property
#     def salaryafterincr(self):
#         return self.salary*self.increment
    
#     @salaryafterincr.setter
#     def salaryafterincr(self, sai):
#         self.increment = sai/self.salary 

# s =  employee()
# print(s.salaryafterincr) 

# print(s.increment)
# s.salaryafterincr  = 2000
# print(s.increment)

# 4. 

# class complex :
#     def __init__(self, r, i):
#         self.real = r
#         self.imaginary  = i
#     def __add__(self, c):
#         return complex(self.real + c.real, self.imaginary + c.imaginary)

#     def __mul__(self, c):
#          mulreal  = self.real*c.real - self.imaginary*c.imaginary
#          mulimg  = self.real*c.imaginary + self.imaginary*c.real
#          return complex(mulreal, mulimg)
#     def __str__(self):
#         if self.imaginary<0:
#             return str(self.real) + "-" + str(self.imaginary) + "i"
#         return str(self.real) + "+" + str(self.imaginary) + "i"
    
# c1 = complex(3, 2)
# c2 = complex(1, 7)
# print(c1+c2)
# print(c1*c2)

# 5. 

# class vector :
#     def __init__(self, vec):
#         self.vec = vec
#     def __str__(self):
#         str1 = ""
#         index = 0
#         for i in self.vec:
#             str1 += str(i)+ "a" + str(index) + " + "
#             index += 1
#         return str1[:-1]
    
#     def __add__(self, vec2):
#         newlist = []
#         for i in range(len(self.vec)):
#             newlist.append(self.vec[i] + vec2.vec[i])
#         return vector(newlist)
    
#     def __mul__(self, vec2):
#         sum = 0
#         for i in range(len(self.vec)):
#             sum  += self.vec[i] + vec2.vec[i]
#         return sum

# v1 =  vector([1, 4, 6])
# v2 = vector([1,6, 9])
# print(v1)
# print(v1+v2)
# print(v1*v2)


# 6. 


# class vector :
#     def __init__(self, vec):
#         self.vec  = vec 

#     def __str__(self):

#         return str(self.vec[0]) + "i" + " + " + str(self.vec[1]) + "j"  + " + " + str(self.vec[2]) + "k"

# v1 = vector([1, 4, 6])
# v2 = vector([1, 6, 9])

# print(v1)
# print(v2)

# 7.

# class vector :
#     def __init__(self, vec):
#         self.vec = vec
#     def __str__(self):
#         str1 = ""
#         index = 0
#         for i in self.vec:
#             str1 += str(i)+ "a" + str(index) + " + "
#             index += 1
#         return str1[:-1]
    
#     def __add__(self, vec2):
#         newlist = []
#         for i in range(len(self.vec)):
#             newlist.append(self.vec[i] + vec2.vec[i])
#         return vector(newlist)
    
#     def __mul__(self, vec2):
#         sum = 0
#         for i in range(len(self.vec)):
#             sum  += self.vec[i] + vec2.vec[i]
#         return sum
    
#     def __len__(self):
#         return len(self.vec)


# v1 =  vector([1, 4, 6])
# v2 = vector([1,6, 9])


# print(len(v1))
# print(len(v2))



