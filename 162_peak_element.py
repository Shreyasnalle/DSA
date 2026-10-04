class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        if len(nums) == 1 :
            return 0
        if nums[0] > nums[1] :
            return 0
        if nums[len(nums) - 1] > nums[len(nums) - 2] :
            return n - 1

        low = 1
        high = len(nums) - 2
        while low <= high :
            mid = (low + high) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1] :
                return mid
            if nums[mid] > nums[mid - 1] :
                low = mid + 1
            else :
                high = mid - 1
        return -1