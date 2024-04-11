class Solution(object):
    def sortArray(self, nums):
        for i in range(len(nums)):
            nums.sort()
            return nums
solution = Solution()
result = solution.sortArray([99,81,2,6,1,0,1,1,23,56,76]) 
print(result)    