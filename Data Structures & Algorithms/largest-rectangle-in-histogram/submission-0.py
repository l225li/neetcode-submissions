class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.insert(0, 0)
        heights.append(0)
        stack = [0]
        result = 0

        for i in range(1, len(heights)):
            if heights[i] > heights[stack[-1]]:
                stack.append(i)
            elif heights[i] == heights[stack[-1]]:
                stack.pop()
                stack.append(i)
            else:
                while stack and heights[i] < heights[stack[-1]]:
                    mid_index = stack.pop()
                    if stack:
                        right_index = i
                        left_index = stack[-1]
                        w = right_index - left_index - 1
                        h = heights[mid_index]
                        result = max(result, w * h)
                stack.append(i)
        
        return result