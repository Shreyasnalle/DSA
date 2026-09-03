class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        res = nums[0]
        cur_max = 1
        cur_min = 1
        for num in nums:
            if num == 0:
                cur_max, cur_min = 1, 1
                res = max(res, 0)
                continue
            temp = cur_max * num
            cur_max = max(num, temp, cur_min * num)
            cur_min = min(num, temp, cur_min * num)
            res = max(res, cur_max)
        return res