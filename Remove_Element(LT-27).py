class Solution(object):
    def removeElement(self, nums, val):
        if not nums:
            return 0
        n = len(nums)
        i = 0
        while(i< n):
            if(nums[i] == val):
                nums.pop(i)
                n -=1
            else:
                i+=1    
        return len(nums)       