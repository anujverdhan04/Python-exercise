class Solution(object):
    def sortArrayByParity(self, nums):
       even = []
       odd = []
       n = len(nums)
       if(n ==1):
            return nums
       for num in nums:
            if(num % 2== 0):
                even.append(num)
            else:
                odd.append(num)
       return  even + odd      

            
        