class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n= len(nums)
        nums.sort()
        for i in range(n):
            if(nums[i] == nums[i+1]):
                return nums[i]
        