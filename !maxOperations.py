# SOLUTION WITH HASHMAP, COME BACK

def maxOperations(nums, k):
    if len(nums) == 1:
        return 0
    i = 0
    j = 1
    operations = 0
    while i < len(nums) and j < len(nums):
        soma = nums[i] + nums[j]
        if i == j:
            j += 1
        elif soma == k:
            operations += 1
            if i < j:
                nums.pop(i)
                j -= 1
                nums.pop(j)
                j -= 1
            else:
                nums.pop(j)
                i -= 1
                nums.pop(i)
                i -= 1

        elif soma < k:
            if nums[i] >= nums[j]:
                j += 1
            else:
                i += 1
        else:
            if nums[i] <= nums[j]:
                j += 1
            else:
                i += 1

    return operations


def main():
    nums = [1, 2, 3, 4]
    k = 5
    nums2 = [3, 1, 3, 4, 3]
    k2 = 6
    print(maxOperations(nums, k))
    print(maxOperations(nums2, k2))


main()
