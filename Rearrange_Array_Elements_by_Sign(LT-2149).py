class Solution(object):
    def rearrangeArray(self, nums):
        pos = [num for num in nums if num >=0]
        neg = [num for num in nums if num <=0]
        result=[]    
        j,k = 0,0
        while(j<len(pos)) and (k<len(neg)):
            result.append(pos[j])
            result.append(neg[k])
            j+=1
            k+=1         

        return result
solution =Solution()
nums = [2,4,-9,-1,5,-4] 
ReA = solution.rearrangeArray(nums) 
print( ReA)
