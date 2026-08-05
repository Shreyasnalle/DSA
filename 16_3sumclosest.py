class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int: 
        nums.sort()
        closed_sum = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)) :
            left = i + 1
            right = len(nums) - 1
            while left < right :
                addition = nums[i] + nums[left] + nums[right]
                if addition == target : 
                    return addition
                elif addition < target :
                    left += 1
                else :
                    right -= 1

                if abs(addition - target) < abs(closed_sum - target) :
                    closed_sum = addition
        return closed_sum