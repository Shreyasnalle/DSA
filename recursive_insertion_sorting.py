def recursive_insertion_sorting(nums, i = 1, n = None) :
    if n is None :
        n = len(nums)
    if i == n :
        return nums
    j = i
    while j > 0 and nums[j - 1] > nums[j] :
        temp = nums[j - 1]
        nums[j - 1] = nums[j]
        nums[j] = temp
        j -= 1
    return recursive_insertion_sorting(nums, i + 1, n)
nums = [7, 1, 9, 2, 10]
sorted_array = recursive_insertion_sorting(nums)
print(f"The sorted array is : {sorted_array}")
