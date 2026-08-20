def longest_sub_array(nums : list[int], k : int) -> tuple[list[int], int] :
    nums.sort()
    count = 0
    array = []
    for i in range(len(nums)) :
        count += nums[i]
        array.append(nums[i])
        if count == k :
            return array 
    if count != k :
        return 0
final_array = longest_sub_array([10, 5, 2, 7, 1, 9], 15)
print(f"final array is : {final_array}")