class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        frequency= {}
        for num in nums :
            if num in frequency :
                frequency[num] += 1
            else :
                frequency[num] = 1
        count = 0
        number = None
        for (key, value) in frequency.items() :
            if value > count :
                count = value
                number = key
        return number   