try:
    n1 = int(input("Num 1:"))
    n2 = int(input("Num 2:"))
    n3 = int(input("Num 3:"))
    n4 = int(input("Num 4:"))

    s = n1 + n2 + n3 + n4

    print("Sum:", s)

except BaseException as e:
    print("error happened")
    print(e)
