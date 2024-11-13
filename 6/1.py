def reverser(strValue: str) -> str:
    reversedStrList = []
    length = len(strValue)
    i = -1
    while i < length - 1:
        i += 1
        reversedStrList.append(strValue[length - (1 + i)])
    return "".join(reversedStrList)


def bubble_sort_f(arr: list, f) -> list:
    for i in range(len(arr)):
        for j in range(0, (len(arr) - i - 1)):
            if f(arr[j], arr[j + 1]) > 0:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def work(strValue: str) -> str:
    words = strValue.split(" ")
    for i, word in enumerate(words):
        words[i] = reverser(word.strip())

    return bubble_sort_f(words, lambda a, b: 1 if a > b else -1)


str1 = "qwerty test1 test2 hello world its working"
str2 = "123456 ok its should work"

print("INPUT:", str1)
print("RESULT:")
print("\n".join(work(str1)))

print("\n\nINPUT:", str2)
print("RESULT:")
print("\n".join(work(str2)))
