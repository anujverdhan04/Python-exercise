class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        mod =1337 
        expo = 0
        for digit in b:
            expo = expo*10 + digit
        return pow(a,expo,mod)    
