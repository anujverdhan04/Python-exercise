
class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num) - 1, -1, -1):
            # Check if the current character is an odd digit
            if int(num[i]) % 2 != 0:
                # Return the substring from the start to this position (inclusive)
                return num[:i + 1]
        # If no odd digit is found, return an empty string
        return ""
        #return max(num)
        