class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        #for num in nums:
            return set(list(itertools.permutations(nums)))
