class Solution:
    def thirdMax(self, nums: List[int]) -> int:


        nums = sorted(set(nums), reverse=True)
        if len(nums) >= 3:
            return nums[2]
        return nums[0]



'''        
        n = len(nums)
        nums.sort()
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                return nums[n-4]
            else:    
                return nums[n-3]    
'''
