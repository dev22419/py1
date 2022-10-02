x = int(input("type the size of your stoage device : "))

print("choose the type of data : ")
print("1) MB")
print("2) GB")
print("3) TB")
print("4) PB")
print("5) EB")
print("6) ZB")
print("7) YB")
print()
a = int(input(">> "))

if a == 1:
    data = "MB"
    y = x + 1000 ** 2
    r = 1024 ** 2
    o = str(y/r)
    size = o[:5]
elif a == 2:
    data = "GB"
    y = x + 1000 ** 3
    r = 1024 ** 3
    o = str(y/r)
    size = o[:5]
elif a == 3:
    data = "TB"
    y = x + 1000 ** 4
    r = 1024 ** 4
    o = str(y/r)
    size = o[:5]
elif a == 4:
    data = "PB"
    y = x + 1000 ** 5
    r = 1024 ** 5
    o = str(y/r)
    size = o[:5]
elif a == 5:
    data = "EB"
    y = x + 1000 ** 6
    r = 1024 ** 6
    o = str(y/r)
    size = o[:5]
elif a == 6:
    data = "ZB"
    y = x + 1000 ** 7
    r = 1024 ** 7
    o = str(y/r)
    size = o[:5]
elif a == 7:
    data = "YB"
    y = x + 1000 ** 8
    r = 1024 ** 8
    o = str(y/r)
    size = o[:5]
else:
    print("please , type a valid option .")
    exit()


print()
print("result : ")
print()
print("if you have a storage device of" , x , data , "then you will have \"" , size , data , "\" on your computer .")
print()
print()