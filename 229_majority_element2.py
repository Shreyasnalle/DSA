class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        quotient = len(nums) // 3 
        frequency = {}
        output = []
        for num in nums :
            if num in frequency :
                frequency[num] += 1
            else :
                frequency[num] = 1
        for key, value in frequency.items() :
            if value > quotient :
                output.append(key)
        return output