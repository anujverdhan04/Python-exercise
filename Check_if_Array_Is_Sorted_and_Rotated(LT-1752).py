class Solution:
    def check(self, nums: List[int]) -> bool:
        if nums == sorted(nums): return True
        k = 1
        n = len(nums)
        while k<n:
            arr = nums[n-k:] + nums[:n-k]
            if arr == sorted(nums):
                return True
            k += 1
        return Falses