class Solution(object):
    def targetIndices(self, nums, target):
        target_index =[]
        for i in range(len(nums)):
            nums.sort()
            if(nums[i] == target):
                target_index.append(i)       
        return target_index 
                