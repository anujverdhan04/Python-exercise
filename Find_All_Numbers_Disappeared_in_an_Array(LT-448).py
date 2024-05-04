class Solution(object):
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        num_set = set(nums)
        all_nums_set = set(range(1 , n+1))
        dis_app = all_nums_set - num_set
        return list(dis_app)

'''        
        n = len(nums)
        nums_set = set(nums)
        disapper_nums =[]
        nums.sort()
        for num in range(1,n+1):
            if num  not in nums:
                disapper_nums.append(num)
        return disapper_nums    
'''
