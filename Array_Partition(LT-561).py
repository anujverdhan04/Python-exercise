class Solution(object):
    def arrayPairSum(self, nums):
        n = len(nums)
        nums.sort()
        sum = 0
        for i in range(0,n,2):
            sum +=  nums[i]
        return sum    
   
        