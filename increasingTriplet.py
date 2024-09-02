"""
Given an integer array nums, 
return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. 
If no such indices exists, return false."""


def increasingTriplet(nums):
    if len(nums) < 3:
        return False
    menor = float('inf')
    maior = float('inf')

    for i in range(len(nums)):
        if nums[i] <= menor:
            menor = nums[i]
        elif nums[i] <= maior:
            maior = nums[i]
        else:
            return True
    return False


def main():
    nums = [1, 2, 3, 4, 5]
    nums2 = [5, 4, 3, 2, 1]
    nums3 = [2, 1, 5, 0, 4, 6]
    nums4 = [5, 1, 6]

    print(increasingTriplet(nums))
    print(increasingTriplet(nums2))
    print(increasingTriplet(nums3))
    print(increasingTriplet(nums4))


main()
