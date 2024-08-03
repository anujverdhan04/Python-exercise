class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        max_area = 0
        heights.append(0)
 
        for i in range(len(heights)):
            # While the stack is not empty and the current bar is shorter than the bar at the stack's top
            while stack and heights[stack[-1]] > heights[i]:

                # Pop the top index from the stack
                h = heights[stack.pop()]
                
                # Calculate the width
                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i
                # Calculate the area with the popped height and update the max_area
                max_area = max(max_area, h * width)
            # Push the current index to the stack
            stack.append(i)
        
        # We appended a 0 height, so we should remove it
        heights.pop()
        
        return max_area