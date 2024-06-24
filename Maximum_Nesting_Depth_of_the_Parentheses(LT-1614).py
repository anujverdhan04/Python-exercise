class Solution:
    def maxDepth(self, s: str) -> int:
        depth =0 
        open1 = 0
        for i in range(len(s)):
            if(s[i]=="("):
                open1 +=1
                depth = max(depth , open1) 
            elif(s[i]== ")" ):
                 open1 -= 1
        return depth                
        