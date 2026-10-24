def countSubsequence(nums : list[int], k : int) -> int :
    count = 0
    n = len(nums)
    def solve(index, current_sum) :
        nonlocal count
        if current_sum == k :
            count += 1
            return 
        if index == n or current_sum > k :
            return
        solve(index + 1, current_sum + nums[index]) 
        solve(index + 1, current_sum)         
    solve(0, 0)
    return count
print(countSubsequence([1, 2, 3, 4, 5], 8))  