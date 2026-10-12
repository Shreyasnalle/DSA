class Solution:
    def beautySum(self, s: str) -> int:
        total = 0
        for i in range(len(s)):
            counts = {}
            for j in range(i, len(s)):
                char = s[j]
                counts[char] = counts.get(char, 0) + 1
                total += max(counts.values()) - min(counts.values())            
        return total