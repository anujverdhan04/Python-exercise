class Solution(object):
    def addBinary(self, a, b):
        
        a_d = int(a,2)
        b_d = int (b,2)
        sum_d  = a_d + b_d
        sum_b = bin(sum_d)[2:]

        return sum_b 
       
                       
        