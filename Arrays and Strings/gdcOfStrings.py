
def gcdOfStrings(str1, str2):
    min_len = min(len(str1), len(str2))
    max_match_len = 0
    match_len = 0
    for i in range(min_len):
        if str1[i] == str2[i]:
            max_match_len += 1
    if max_match_len == 0:
        return ""

    for j in range(1, max_match_len+1):
        if len(str1) % j == 0 and len(str2) % j == 0:
            match_len = j
    if len(str1) == len(str2) and len(str1) == max_match_len:
        return str1
    for k in range(0, len(str1), match_len):
        if ((str2[:match_len] != str1[k:k+match_len]) or (str2[:match_len] != str1[k:k+match_len])):
            return ""
    for l in range(0, len(str2), match_len):
        if (str1[:match_len] != str2[l:l+match_len]):
            return ""
    return (str1[:match_len])


def main():
    gdc = gcdOfStrings(str1="ABABAB", str2="ABAB")
    print(gdc)


main()
