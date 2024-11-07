def reverser(strValue: str) -> str:
    reversedStrList = []
    length = len(strValue)
    i = -1
    while i < length - 1:
        i += 1
        reversedStrList.append(strValue[length - (1 + i)])
    return "".join(reversedStrList)


str1 = "qwerty"
str2 = "123456"

print(str1, reverser(str1))
print(str2, reverser(str2))
