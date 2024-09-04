def findDifference(nums1,nums2):
    in1 = {}
    in2 = {}
    result = [[],[]]
    for i in range(len(nums1)):
        if nums1[i] not in nums2:
            in1[nums1[i]] = i
    for j in range(len(nums2)):
        if nums2[j] not in nums1:
            in2[nums2[j]] = j
            
    for chave,valor in in1.items():
        result[0].append(chave)

    for chave,valor in in2.items():
        result[1].append(chave)

        
    return result

def main():
    nums1 = [1,2,3,3]
    nums2 = [1,1,2,2]
    print(findDifference(nums1,nums2))
    
main()