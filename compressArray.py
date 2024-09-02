"""Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. 
Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space."""


def compress(chars):
    s = ""
    char = ""
    count = 1
    for i in range(len(chars)):
        if i == 0:
            char = chars[0]
            if i == len(chars) - 1:
                if count == 1:
                    s += char
                else:
                    s += char+f"{count}"
        else:
            if chars[i] == char:
                count += 1
                if i == len(chars) - 1:
                    if count == 1:
                        s += char
                    else:
                        s += char+f"{count}"
            else:
                if count == 1:
                    s += char
                else:
                    s += char+f"{count}"
                    count = 1
                char = chars[i]
                if i == len(chars) - 1:
                    s += char
    for i, char in enumerate(s):
        chars[i] = char
    return len(s)


def main():
    chars = ["a", "b", "c"]
    print(compress(chars))


main()
