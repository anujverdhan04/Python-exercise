class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n= len(nums)
        nums.sort()
        element = nums[n-k]
        return element
        