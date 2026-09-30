class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        def division(nums, mid) :
            add = 0
            for num in nums :
                add += (num + mid - 1) // mid 
            return add
        
        low = 1 
        high = max(nums)
        ans = high 

        while low <= high :
            mid = (low + high) // 2
            add = division(nums, mid)
            if add <= threshold :
                ans = mid
                high = mid - 1
            else :
                low = mid + 1
        
        return ans