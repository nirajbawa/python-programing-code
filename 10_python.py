# 1.

# class programmer :
#     company = "microsoft"
#     def __init__(self, name, product):
#           self.name = name
#           self.product = product
    
#     def printmthod(self):
#         print(self.name + "\n" + self.product)

# harry = programmer("niraj", "windows")
# harry = programmer("ram", "github")
# harry.printmthod()


# 2.

# class calculator :
#     def __init__(self,num):
#         self.number = num
#     def sq(self):
#         print("the value of " + str(self.number) + " square is " + str(self.number **2) )
#     def sqr(self):
#         print("the value of " + str(self.number) + " square root is " +  str(self.number **0.5))
#     def cu(self):
#         print("the value of " + str(self.number) + " cube is " + str(self.number **3))


# cal =  calculator(2)
# cal.sq()
# cal.sqr()
# cal.cu()


# 3.

# class sample :
#     a = "niraj"

# obj = sample()
# obj.a= "ram"
# sample.a =  "rampal"

# print(sample.a)
# print(obj.a)

# 4.
from win32com.client import Dispatch

# class hello:
#     @staticmethod
#     def hell():
#         speak = Dispatch("SAPI.SpVoice")
#         speak.Speak("he! hello user.....")
#         converter.setProperty('rate', 50) 

# sa = hello()
# hello.hell()

# 5.
# class train :
#     def __init__(self,  name , fare,  seats):
#         self.name = name
#         self.fare =  fare
#         self.seats = seats
#     def getstatus(self):
#         print("the name of the train is " +  self.name)
#         print("the seats avilable in the train are " + str(self.seats))

#     def getinfo(self):
#         print("the price of the ticket is : rs " + str(self.fare))
    
#     def getticket(self):
#         if(self.seats>0):
#             print("your ticket has been booked! you seat number is " + str(self.seats - 1))
#             self.seats = self.seats - 1
#         else:
#             print("sorry thid train is full! your seat number is ")
#     def cancelticket(self):
#         self.seats = self.seats + 1
#         print("the seats avilable in the train are " + str(self.seats))


# a = train("chainai express", 80, 10)


# a.getstatus()

# a.getticket()

# a.getinfo()

# a.cancelticket()



#  6.


class sample :
    def __init__(slf, name):
        slf.name =  name

obj = sample("niraj")
print(obj.name)