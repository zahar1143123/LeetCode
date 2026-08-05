class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        mx = 0
        for idx, height in enumerate(heights):
            start = idx
            while stack and stack[-1][1]>height:
                pr_idx, pr_height = stack.pop()
                mx= max(mx, pr_height*(idx-pr_idx))
                start=pr_idx
            stack.append((start, height))
        
        for idx, height in stack:
            mx=max(mx, height*(len(heights)-idx))

        return mx

