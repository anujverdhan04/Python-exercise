class Solution(object):
    def search(self, nums, target):
        for i in range(len(nums)):
            if(nums[i]==target):
                return i
        return -1
solution = Solution()
nums = [-1,0,3,5,9,12]
target = 9

print(solution.search(nums,target))