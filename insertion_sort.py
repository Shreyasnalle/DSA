def insertion_sort(nums : list) -> list :
    for i in range(len(nums)) :
        j = i
        while j > 0 and nums[j - 1] > nums[j] :
            temp = nums[j - 1]
            nums[j - 1] = nums[j]
            nums[j] = temp
            j -= 1
    print(f"the final sorted array is : {nums}")
insertion_sort([21,2,5,1,9])