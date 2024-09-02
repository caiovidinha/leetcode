def isSubsequence(s: str, t: str) -> bool:
    if s == "":
        return True
    if t == "":
        return False
    index_s = 0
    index_t = 0
    while index_t < len(t):
        if s[index_s] == t[index_t]:
            index_s += 1
            if index_s >= len(s):
                return True
        index_t += 1

    return False


def main():
    s = ""
    t = "ahcjb"
    print(isSubsequence(s, t))


main()
