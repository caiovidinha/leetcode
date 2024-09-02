def merge(nums1, m, nums2, n):
    i = 0
    j = 0
    nums_aux = []
    for inc in range(m):
        nums_aux.append(nums1[inc])

    while i+j <= m+n-1:
        if j >= n:
            nums1[i+j] = nums_aux[i]
            i += 1
            continue
        if i >= m:
            nums1[i+j] = nums2[j]
            j += 1
            continue

        if nums_aux[i] <= nums2[j]:
            nums1[i+j] = nums_aux[i]
            i += 1
        else:
            nums1[i+j] = nums2[j]
            j += 1
    return


def main():
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    merge(nums1, m, nums2, n)


main()
