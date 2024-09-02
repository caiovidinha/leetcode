def reverseVowels(s):
    vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    s_list = list(s)
    vogais_in_s = []
    vogais_index = []
    for i, c in enumerate(s_list):
        if c in vogais:
            vogais_in_s.append(c)
            vogais_index.append(i)

    for vogal in vogais_in_s:
        s_list[vogais_index.pop()] = vogal

    return ''.join(s_list)


def main():
    s = 'Aa'
    print(reverseVowels(s))


main()
