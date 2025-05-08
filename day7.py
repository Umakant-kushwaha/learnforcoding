a = int(input("first num"))
x = input("* + - /")
b = int(input("second num"))
if (x == "*"):
    c = a*b
    print("ans =", c)
elif (x == "-"):
    c = a-b
    print("ans =", c)    
elif (x == "+"):
    c = a+b
    print("ans =", c)
elif (x == "/"):
    c = a/b
    print("ans =", c)