class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        addition = 0
        seen = {
            0 : 1
        }
        count = 0
        for num in nums:
            addition += num
            if (addition - k) in seen:
                count += seen[addition - k]
            if addition in seen:
                seen[addition] += 1
            else:
                seen[addition] = 1
        return count 
        