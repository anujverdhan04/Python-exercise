class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        st = []
        for digit in num:
            while k>0 and st and st[-1] >digit:
                st.pop()
                k-=1
            st.append(digit)
        while k > 0:
            st.pop()
            k -= 1

        result = ''.join(st).lstrip('0')
        # Return "0" if result is empty, otherwise return the result
        return result if result else "0"     