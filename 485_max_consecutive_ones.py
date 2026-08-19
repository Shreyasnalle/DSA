class Solution:
    def findMaxConsecutiveOnes(self, nums : list[int]) -> int:
        count_ones = 0
        maximum_ones = 0
        for num in nums :
            if num == 1 :
                count_ones += 1
                maximum_ones = max(maximum_ones, count_ones)
            else :
                count_ones = 0
        return maximum_ones
