class Solution(object):
    def majorityElement(self, nums):
        nums.sort()
        n = len(nums)
        return nums[n//2]
'''
          n = len(nums)
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if (nums[i] == nums[j]):
                    count +=1
            if(count >(n//2)):
                return nums[i]
        return -1         
'''             

        