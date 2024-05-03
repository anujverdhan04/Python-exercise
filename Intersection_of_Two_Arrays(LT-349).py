class Solution(object):
    def intersection(self, nums1, nums2):
        set_1 = set(nums1)
        set_2 = set(nums2)
        set_inc = set_1.intersection(set_2)
        list_inc = list(set_inc)
        return list_inc
'''       
            nums_intersection = [value for value in nums1 if value in nums2]
            return nums_intersection
'''

'''     n = len(nums1)
        m = len(nums2)
        for i in range(n):
            for j in range(m):
                if(nums1[i] == nums2[j]):
                    return nums1[i]
'''        