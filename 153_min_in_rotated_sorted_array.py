class Solution:
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        position_max_element = nums.index(max(nums))
        last_position = n - 1
        rotated = (position_max_element + 1) % n

        original_nums = [0] * n
        for i in range(len(nums)) :
            original_nums[i] = nums[(i + rotated) % n] 
        
        return original_nums[0]