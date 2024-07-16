class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        if dividend == divisor:
            return 1

        sign = (dividend > 0) == (divisor > 0)

        dividend, divisor = abs(dividend), abs(divisor)
        
        ans = 0

        while dividend >= divisor:
            temp, count = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                count <<= 1
            dividend -= temp
            ans += count

        if not sign:
            ans = -ans

        if ans < INT_MIN:
            return INT_MIN
        if ans > INT_MAX:
            return INT_MAX

        return ans
