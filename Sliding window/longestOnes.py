def longestOnes(nums, k):
    l = 0
    max_num = 0

    for r in range(len(nums)):
        k -= 1 - nums[r]

        if k < 0:
            k += 1 - nums[l]
            l += 1
        else:
            max_num = max(max_num, r - l + 1)

    return max_num


def main():
    nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    k = 3
    print(longestOnes(nums, k))


main()
