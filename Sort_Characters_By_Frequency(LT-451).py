class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        
        # Sort characters by frequency in descending order, then by the character itself
        sorted_chars = sorted(count.items(), key=lambda item: (-item[1], item[0]))
        
        # Construct the final sorted string
        result = ''.join([char * freq for char, freq in sorted_chars])
        
        return result

'''        
        n = len(s)
        for i in range(n):
            count = 0
            if(s[i] == s[i+1]):
                count +=1
            sorted_s = sorted(count.items() , key = lambda item:(item[-1] ,item[0])    
                return s 
'''