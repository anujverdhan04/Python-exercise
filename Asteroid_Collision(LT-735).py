class Solution:
    def asteroidCollision(self, ast: List[int]) -> List[int]:
        result = []
        n= len(ast)
        for i in range(n):
            if ast[i] > 0:
                result.append(ast[i])
            else:
                while result and result[-1] > 0 and result[-1] < abs(ast[i]):
                    result.pop()
                if result and result[-1] == abs(ast[i]):
                    result.pop()
                elif not result or result[-1] < 0:
                    result.append(ast[i])
        return result

'''        
        n= len(ast)
        result = []
        for i in range(n):
            if(i<(i+1)):
                result.append(ast[i])
                return result
            elif( i== (i+1)):
                result.append()
            return result
'''            