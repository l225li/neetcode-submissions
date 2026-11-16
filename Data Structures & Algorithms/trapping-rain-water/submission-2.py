class Solution:
    def trap(self, height: List[int]) -> int:
        stack = [0]
        result = 0

        for i in range(1, len(height)):
            if height[i] < height[stack[-1]]:
                stack.append(i)
            elif height[i] == height[stack[-1]]:
                stack.pop()
                stack.append(i)
            else:
                while stack and height[i] > height[stack[-1]]:
                    mid_height = height[stack.pop()]
                    if stack:
                        right_height = height[i]
                        left_height = height[stack[-1]]
                        h = min(right_height, left_height) - mid_height
                        w = i - stack[-1] - 1
                        result += h * w
                stack.append(i)
        
        return result
        