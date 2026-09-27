class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        position_max = nums.index(max(nums))
        total_length = n - 1 
        left_rotation = total_length - position_max

        original_nums = [0] * n
        for i in range(n):
            original_nums[i] = nums[(i - left_rotation) % n]

        low = 0
        high = len(nums) - 1
        while low <= high :
            mid = (low + high) // 2
            if original_nums[mid] == target :
                return (mid - left_rotation) % n
            elif original_nums[mid] > target :
                high = mid - 1
            else :
                low = mid + 1
        return -1