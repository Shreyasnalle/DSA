def linear_search(nums : list, k : int) -> int :
    for i in range(len(nums)) :
        if nums[i] == k :
            return i
location = linear_search([0, 24, -1, 12], 24)
print(f"location : {location}")
