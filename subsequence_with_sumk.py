def checkSubsequenceSum(nums: list[int], k: int) -> bool:
    n = len(nums)
    def solve(index, current_sum):
        if current_sum == k:
            return True
        if index == n or current_sum > k:
            return False
        pick = solve(index + 1, current_sum + nums[index])
        if pick:
            return True
        dont_pick = solve(index + 1, current_sum)
        return dont_pick
    return solve(0, 0)
print(checkSubsequenceSum([1, 2, 3, 4, 5], 8))
print(checkSubsequenceSum([4, 3, 9, 2], 10))