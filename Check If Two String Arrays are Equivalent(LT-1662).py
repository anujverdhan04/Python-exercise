class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        a =""
        for s in word1:
            a += s
        b=""    
        for s in word2:
            b += s
        if(a == b):
            return True
        else:
            return False

