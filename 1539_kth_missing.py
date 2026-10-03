class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        missing = []
        for num in range(1, len(arr) + k + 1) :
            if num not in arr :
                missing.append(num)
                if len(missing) == k :
                    return num