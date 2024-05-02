class Solution(object):
    def construct2DArray(self, original, m, n):
        if len(original) != m * n:
            return []
        result = [[0] * n for _ in range(m)]
        for i in range(m):
            result[i] = original[i * n : (i + 1) * n]
        
        return result
solution = Solution()
original = [2,3,4,2,5,6,7,8,9]  
m =3
n=3 
result = solution.construct2DArray(original, m, n)
print(result)