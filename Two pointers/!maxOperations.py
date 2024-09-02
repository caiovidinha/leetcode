def maxOperationsSort(nums, k):
    i = 0
    j = len(nums)-1
    operations = 0
    nums.sort()
    while i < j:
        soma = nums[i] + nums[j]
        if soma == k:
            operations += 1
            i+=1
            j-=1

        elif soma < k:
            i+=1
        else:
            j-=1

    return operations

# SOLUTION WITH HASHMAP, COME BACK
def maxOperationsHash(nums, k):
    pass


def main():
    nums = [1, 2, 3, 4]
    k = 5
    nums2 = [3, 1, 3, 4, 3]
    k2 = 6
    print(maxOperationsSort(nums, k))
    print(maxOperationsSort(nums2, k2))


main()
