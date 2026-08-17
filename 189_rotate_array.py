def rotate(self, nums : list[int], k : int) -> None :
    n = len(nums)
    k %= n 
    for i in range(k) :
        temp = nums[len(nums) - 1]
        a = n - 1
        b = n - 2
        while nums[0] is None :
            nums[a] = nums[b]
            a -= 1
            b -= 1
        nums[0] = temp