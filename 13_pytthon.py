# practice set 

# 2.


# while(True):
    

#     name = raw_input("inter your name")
#     mark = input("enter your marks")
#     phone = input("enter your number")

    
#     try:

#         mark = int(mark)

#         phone = int(phone)
#         template = "the name of th  student is {}, his  marks are {} and phone number is {} "

#         output = template.format(name, mark, phone)

#         print(output)

#     except Exception as f:
#         print(f)

# 2.


# l = [str(i*7 )for i in range(1, 11)]
# print(l)

# vertical =  "\n".join(l)

# print(vertical)

# 3.

# l = [11,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,56,67,976]

# a = filter(lambda a: a%5==0, l)
# print(list(a))


# 4.
# from functools import reduce

# l =  [3,8,4,2,5]

# a = reduce(max, l)


# print(a)

# print(max(7, 34))


# 5.

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
if __name__ == "__main__":
    app.run(debug=True)