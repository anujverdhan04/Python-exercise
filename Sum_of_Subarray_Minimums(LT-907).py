class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        left = [0] * n
        right = [0] * n
        stack = []
        
        # Compute the left boundaries
        for i in range(n):
            count = 1
            while stack and stack[-1][0] > arr[i]:
                count += stack.pop()[1]
            left[i] = count
            stack.append((arr[i], count))
        
        stack = []
        
        # Compute the right boundaries
        for i in range(n-1, -1, -1):
            count = 1
            while stack and stack[-1][0] >= arr[i]:
                count += stack.pop()[1]
            right[i] = count
            stack.append((arr[i], count))
        
        # Compute the sum of minimums of all subarrays
        result = 0
        for i in range(n):
            result += arr[i] * left[i] * right[i]
        
        return result % (10**9 + 7)

'''
    def sumSubarrayMins(self, arr: List[int]) -> int:
        result = []
        
        def backtrack(start, path):
            result.append(path)
            for i in range(start, len(arr)):
                backtrack(i + 1, path + [arr[i]])
        
        backtrack(0, [])
        
        # Remove the empty subset
        result = [subset for subset in result if subset]
        
        # Calculate the sum of minimums of all subarrays
        total_sum = 0
        for subset in result:
            total_sum += min(subset)
        
        return total_sum
'''