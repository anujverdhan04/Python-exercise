class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count_ones = s.count('1')
        count_zeros = s.count('0')

        # The maximum odd binary number will have:
        # - All '1's except one at the beginning
        # - All '0's in the middle
        # - One '1' at the end
        return '1' * (count_ones - 1) + '0' * count_zeros + '1'