class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        n = len(nums)
        result = [-1] * n 
        stack = []

        # Iterate twice over the array to handle the circular nature
        for i in range(2 * n):
            current_index = i % n
            while stack and nums[stack[-1]] < nums[current_index]:
                index = stack.pop()
                result[index] = nums[current_index]
            if i < n:
                stack.append(current_index)

        return result
'''        
        n = len(nums)
        result = [-1] * n  # Initialize result array with -1

        for i in range(n):
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    result[i] = nums[j]
                    break

        return result
'''