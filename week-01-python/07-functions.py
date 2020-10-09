# 함수 functions
# 입력값 parameters, 반환값 return

def hello_friends(name):
    print("Hi, {}".format(name))

name1 = "sunyoung"
name2 = "dayoung"
name3 = "doyoung"
name4 = "hara"
name5 = "sunyoung"
name6 = "dayoung"
name7 = "doyoung"
name8 = "hara"
# print("Hello, {}".format(name1))
# print("Hello, {}".format(name2))
# print("Hello, {}".format(name3))
# print("Hello, {}".format(name4))
# print("Hello, {}".format(name5))
# print("Hello, {}".format(name6))
# print("Hello, {}".format(name7))
# print("Hello, {}".format(name8))

hello_friends(name1)
hello_friends(name2)
hello_friends(name3)
hello_friends(name4)
hello_friends(name5)
hello_friends(name6)
hello_friends(name7)
hello_friends(name8)

# 1) 입력값 o, 반환값 o
def sum(a, b):
    return a + b

# 2) 입력값 o, 반환값 x
def hello_friends(name):
    print("Hi, {}".format(name))

# 3) 입력값 x, 반환값 o
def return_1():
    return 1

# 4) 입력값 x, 반환값 x
def hello_world():
    print("hello world")

num_1 = return_1()
print(num_1)
