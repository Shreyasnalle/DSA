def bubble_sorting(nums : list) -> list :
    for i in range(len(nums) - 1, 0, -1) :
        for j in range(0, i) :
            if nums[j] > nums[j + 1] :
                store =  nums[j + 1]
                nums[j + 1] = nums[j]
                nums[j] = store
    print(f"the final sorted array by bubble sort is : {nums}")
    return nums
bubble_sorting([7, 1, 10, 0, 24])