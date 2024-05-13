class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        distinct_nums1 = set(nums1)
        distinct_nums2 = set(nums2)
        
        answer0 = list(distinct_nums1 - distinct_nums2)
        answer1 = list(distinct_nums2 - distinct_nums1)
        
        return [answer0, answer1]

