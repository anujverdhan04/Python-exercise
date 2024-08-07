class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq = Counter(nums)
        result = sum(num for num , count in freq.items() if count ==1)
        return result

'''
        n =len(nums)
        tpp =[]
        i=0
        while i<(n-1):
            if(nums[i]!=nums[i+1]):
                tpp.append(nums[i])
            i+=1
        if(nums[-1] != nums[-2]):
                tpp.append(nums[-1])

        result = sum(tpp)
        return result        
'''
                
        