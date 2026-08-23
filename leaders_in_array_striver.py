def leader_of_the_array(nums : list[int]) -> list[int] :
    leader_array = []
    for i in range(len(nums) - 1, -1, -1) :
        if i == len(nums) - 1 :
            leader_array.append(nums[i])
        else :
            j = i + 1
            is_leader = True
            while j < len(nums) : 
                if nums[i] <= nums[j] :
                    is_leader = False
                    break
                j += 1
            if is_leader :
                leader_array.append(nums[i])
    leader_array.reverse()
    return leader_array
array = leader_of_the_array([1, 2, 5, 3, 1, 2])
print(f"final leader array : {array}")
