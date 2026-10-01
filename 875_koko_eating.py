class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def calculation(mid):
            total_hours = 0
            for pile in piles:
                total_hours += (pile + mid - 1) // mid
            return total_hours

        low = 1
        high = max(piles)
        ans = high

        while low <= high:
            mid = (low + high) // 2
            hours_needed = calculation(mid)
            if hours_needed <= h:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans