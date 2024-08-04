class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        n = len(matrix)
        m = len(matrix[0])
        max_area = 0
        
        # Initialize the prefix sum matrix
        psum = [[0] * m for _ in range(n)]
        
        # Fill the prefix sum matrix
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == '1':
                    if i == 0:
                        psum[i][j] = 1
                    else:
                        psum[i][j] = psum[i-1][j] + 1
                else:
                    psum[i][j] = 0
        
        # Function to calculate the largest rectangle in a histogram
        def largestRectangleArea(heights: List[int]) -> int:
            stack = []
            max_area = 0
            heights.append(0)  # Add a sentinel value to handle remaining bars in the stack
            
            for i in range(len(heights)):
                while stack and heights[stack[-1]] > heights[i]:
                    h = heights[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)
                
            heights.pop()  # Remove the sentinel value
            return max_area
        
        # Calculate the maximum area for each row in the prefix sum matrix
        for i in range(n):
            max_area = max(max_area, largestRectangleArea(psum[i]))
        
        return max_area
