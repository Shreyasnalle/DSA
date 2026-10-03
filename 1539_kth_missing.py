class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        missing = []
        for num in range(1, len(arr) + k + 1) :
            if num not in arr :
                missing.append(num)
                if len(missing) == k :
                    return num

class Solution:
    def findKthPositive(self, arr: list[int], k: int) -> int:
        low = 0
        high = len(arr) - 1
        
        while low <= high:
            mid = (low + high) // 2
            missing = arr[mid] - (mid + 1)
            
            if missing < k:
                low = mid + 1
            else:
                high = mid - 1

        return low + k
