class Solution(object):
    def searchRange(self, nums, target):
        try:
            start =nums.index(target)
            end = len(nums) - 1 - nums[::-1].index(target)
            return (start),(end)
        except ValueError:
            return[-1,-1]               
        