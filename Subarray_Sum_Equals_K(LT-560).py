class Solution(object):
    def subarraySum(self, nums, k):
        n=  len(nums)
        count = 0  
        for i in range(n):
            sum = 0
            for j in range (i , n):
                sum += nums[j]
                if (sum == k ):
                    count+=1        
        return count
           
       

        