class Solution(object):
    def isPossibleToSplit(self, nums):
        if len(nums) % 2 == 0:
            half_length = len(nums) // 2
            nums1 = nums[:len(nums)//2]
            nums2 = nums[len(nums)//2:]
            return True
        else:
            return False 