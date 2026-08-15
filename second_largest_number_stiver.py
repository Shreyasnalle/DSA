def second_largest_number(nums : list) -> int :
    nums.sort()
    second_last = len(nums) - 2
    return nums[second_last]
second_number = second_largest_number([21, 12, 45])
print(f"second largest number is: {second_number}")

def without_sorting(nums : list) -> int :
    largest = nums[0]
    second = None
    for num in nums :
        if num > largest :
            largest = num 
    for num in nums :
        if num != largest :
            if second is None or num > second :
                second = num
    return second
second_number_without_sorting = without_sorting([21, 12, 45])
print(f"the second largest number without sorting is : {second_number_without_sorting}")