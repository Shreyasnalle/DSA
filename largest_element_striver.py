def largest_number_in_array(nums : list) -> int:
    maximum = nums[0]
    for num in nums :
        if num >= maximum :
            maximum = num
    return maximum
largest_number = largest_number_in_array([10, 7, 24])
print(f"the largest number is : {largest_number}")