class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def calculation(weights, days, weight) :
            days = 1
            weighing_machine = 0
            for i in range(len(weights)) :
                if weighing_machine + weights[i] <= weight :
                    weighing_machine += weights[i]
                else :
                    days += 1
                    weighing_machine = weights[i]
            return days
        
        low = max(weights)
        high = sum(weights)
        minimum_weight = high
        while low <= high :
            weight = (low + high) // 2
            calulated_days = calculation(weights, days, weight)
            if calulated_days <= days :
                minimum_weight = weight
                high = weight - 1
            else :
                low = weight + 1
        return minimum_weight