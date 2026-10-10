class Solution:
    def maxDepth(self, s: str) -> int:
        current_depth = 0
        maximum_depth = 0

        for char in s :
            if char == "(" :
                current_depth += 1
                maximum_depth = max(maximum_depth, current_depth)
            elif char == ")" :
                current_depth -= 1
        return maximum_depth