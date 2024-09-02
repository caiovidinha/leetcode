def reverseWords(s):
    list = s.split(" ")
    result = []
    for i in range(len(list)):
        a = list.pop()
        if a != "":
            result.append(a)
    return ' '.join(result)


def main():
    s = "  hello world  "
    print(reverseWords(s))


main()
