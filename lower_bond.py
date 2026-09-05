def lower_bond(nums : list[int], target : int) -> int :
    low = 0
    high = len(nums) - 1
    ans = len(nums)
    while low <= high :
        mid = (low + high) // 2
        if nums[mid] >= target :
            ans = mid 
            high = mid - 1 
        else :
            low = mid + 1
    return ans
answer = lower_bond([1, 2, 4, 4, 5, 7], 4)
print(answer)