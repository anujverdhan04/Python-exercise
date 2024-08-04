class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        lists = []
        for i in range(n-k+1):
            maximum= nums[i]
            for j in range(i, (i+k)):
                maximum = max(maximum , nums[j])
            lists.append(maximum)
        return lists        
        