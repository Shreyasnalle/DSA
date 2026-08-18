class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        insert_position = 0
        for i in range(len(nums)) :
            if nums[i] != 0 :
                nums[insert_position], nums[i] = nums[i], nums[insert_position]
                insert_position += 1