class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        if m * k > len(bloomDay) :
            return -1
        def bloom(bloomDay, m, k, day) :
            count = 0
            bouquets = 0
            for bloomday in bloomDay :
                if day >= bloomday :
                    count += 1
                    if count == k :
                        bouquets += 1
                        count = 0
                else :
                    count = 0
            return bouquets
        
        low = min(bloomDay)
        high = max(bloomDay)
        final_ans = -1

        while low <= high :
            mid = (low + high) // 2
            bouquets = bloom(bloomDay, m, k, mid)
            if bouquets >= m :
                final_ans = mid
                high = mid - 1
            else :
                low = mid + 1
        return final_ans
