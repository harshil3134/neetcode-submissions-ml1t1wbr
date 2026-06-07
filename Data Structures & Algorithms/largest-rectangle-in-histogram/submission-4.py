class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [] # Stores pairs of (index, height)
        max_area = 0
        
        for i, h in enumerate(heights):
            start = i
            
            # The moment we see a SHORTER bar, we must pop and calculate areas
            while stack and stack[-1][1] > h:
                popped_index, popped_height = stack.pop()
                
                # Calculate the width: current index minus where the popped bar started
                width = i - popped_index
                area = popped_height * width
                max_area = max(max_area, area)
                
                # Crucial Step: The incoming shorter bar can backward-extend 
                # all the way to the index of the bar we just popped!
                start = popped_index
                
            # Push the current bar with its earliest possible start index
            stack.append((start, h))
            
        # Clear out any remaining bars that survived until the end of the histogram
        for start_index, h in stack:
            width = len(heights) - start_index
            area = h * width
            max_area = max(max_area, area)
            
        return max_area