def mergeAlternately(word1, word2):
    i = 0
    j = 0
    merged = []
    while i + j < len(word1) + len(word2):
        if (i == len(word1)):
            return ''.join(merged) + word2[j:len(word2)]

        if (j == len(word2)):
            return ''.join(merged) + word1[i:len(word1)]

        merged.append(word1[i])
        merged.append(word2[j])
        i += 1
        j += 1

    return ''.join(merged)


def main():
    word1 = "abccaiovidinha"
    word2 = "pqrcaio"

    final = mergeAlternately(word1, word2)
    print(final)


main()
