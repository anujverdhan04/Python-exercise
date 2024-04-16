class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n
        nums[:] = nums[-k:] + nums[:-k]
        return nums
'''class Solution(object):
    def rotate(self, nums, k):
        for i in range(k):
            nums.insert(0, nums.pop(-1))   
        return nums
'''
        -