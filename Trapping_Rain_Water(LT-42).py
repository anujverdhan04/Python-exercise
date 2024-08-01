class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n
        
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])
        
        right_max[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])
        
        trapped_water = 0
        for i in range(n):
            trapped_water += min(left_max[i], right_max[i]) - height[i]
        return trapped_water

'''       
        n = len(height)
        count =0
        for i in range(n-1):
            left = i
            right = i+2
            if(left ==0 and right == 0):
                return 1
            elif(left <= right):
                count+=1
            else:
                count +=1
            return count       
'''

 
        