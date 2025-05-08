# a = 5
# b = 10
# print("a+b=", a+b)
# print("-"*40)
# a = 50
# b = 30
# print("a + b = ", a+b )

# def si(p,r,t):
#     a = p*r*t /100
#     print(a)

# def total(a,b):
#     c = a + b
#     print(a)

# total(10,15)

# total(45,154)

a = int(input("first num"))
x = input("* + - /")
b = int (input(" sec num"))
if (x == "*"):
    c = a*b
    print("ans =", c)
elif(x == "+"):
    c = a+b
    print("ans =", c)
elif(x == "-"):
    c = a-b
    print("ans =", c)
elif(x == "/"):
    c = a/b
    print("ans =", c)
