class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        temp_nums = []
        for num in nums:
            num = num **2
            temp_nums.append(num)
            temp_nums.sort()
        return temp_nums

            
                 
solution = Solution()
nums = [2,3,-1,4,6]
result = solution.sortedSquares(nums)
print (result)        