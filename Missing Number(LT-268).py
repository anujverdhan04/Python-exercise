class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        sums = n*(n+1)//2
        for i in range(n):
            nums_sum = sum(nums)
            number = (sums - nums_sum)
            return number

            

        