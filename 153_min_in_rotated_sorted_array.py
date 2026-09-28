class Solution:
    def findMin(self, nums: list[int]) -> int:
        n = len(nums)
        position_max_element = nums.index(max(nums))

        rotated = (position_max_element + 1) % n

        original_nums = [0] * n
        for i in range(len(nums)) :
            original_nums[i] = nums[(i + rotated) % n] 
        
        return original_nums[0]
# finding max -> o(n), rotating to original -> o(n)

class Solution:
    def findMin(self, nums: list[int]) -> int:
        low = 0
        high = len(nums) - 1
        
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
                
        return nums[low]
# o(logn)
