def maxVowels(s, k):
    vowels = "aeiou"
    indices = [float("-inf")]
    maxCount = float("-inf")
    for i in range(len(s)):
        if len(indices) >= 1 and indices[0] <= i-k:
            indices.pop(0)
        if s[i] in vowels:
            indices.append(i)
        if len(indices) > maxCount:
            maxCount = len(indices)
    return maxCount


def main():
    s = "leetcode"
    k = 3
    print(maxVowels(s, k))


main()
