class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]] :
        result = []
        nums.sort()
        def backtrack(index, current) :
            if index == len(nums) :
                result.append(list(current))
                return
            current.append(nums[index])
            backtrack(index + 1, current)
            current.pop()
            while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                index += 1
            backtrack(index + 1, current)
        backtrack(0, [])
        return result