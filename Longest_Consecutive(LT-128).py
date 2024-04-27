class Solution(object):
    def longestConsecutive(self, nums):
       long_conse = 1
       n = len(nums)
       if not nums:
            return 0
       nums.sort()      
       for i in range(n-1):
            if(nums[i] +1 == nums[i+1]):
                long_conse +=1
       return long_conse 
solution = Solution()
nums = [-1,-1,0,5,2,3,6,4,7]
nums.sort()
print(nums)
pg = solution.longestConsecutive(nums)
print(pg)