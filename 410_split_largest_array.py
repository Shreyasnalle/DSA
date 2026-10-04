class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def count_subarrays(nums, mid) : 
            subarrays = 1
            current_sum = 0
            for num in nums :
                if current_sum + num <= mid :
                    current_sum += num
                else :
                    subarrays += 1
                    current_sum = num
            return subarrays
        low = max(nums)
        high = sum(nums)
        ans = high
        while low <= high:
            mid = (low + high) // 2
            subarrays_needed = count_subarrays(nums, mid)
            if subarrays_needed <= k:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def subarrays_formed(k, mid) :
            subarray_count = 1
            count = 0
            for num in nums :
                if count + num <= mid :
                    count += num
                else :
                    subarray_count += 1
                    count = num
            return subarray_count

        low = max(nums)
        high = sum(nums)
        answer = high
        while low <= high :
            mid = (low + high) // 2
            subarray = subarrays_formed(k, mid)
            if subarray <= k :
                answer = mid 
                high = mid - 1
            else :
                low = mid + 1
        return answer