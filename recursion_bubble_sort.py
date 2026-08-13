def recursion_bubble_sort(nums, n = None) :
    if n is None :
        n = len(nums)
    if n == 1 or n == 0 :
        return nums
    for i in range(1, n) :
        if nums[i - 1] > nums[i] :
            temp = nums[i - 1]
            nums[i - 1] = nums[i]
            nums[i] = temp
    return recursion_bubble_sort(nums, n - 1)
array = [7, 1, 9, 2, 10]
sorted_array = recursion_bubble_sort(array)
print(f"The final sorted array is : {sorted_array}")