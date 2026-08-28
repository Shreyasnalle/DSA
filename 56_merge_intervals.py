class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        if not intervals :
            return []
        intervals.sort(key = lambda x : x[0])
        minimum = intervals[0][0]
        maximum = intervals[0][1]
        final_array = []
        for i in range(1, len(intervals)) :
            if intervals[i][0] <= maximum :
                minimum = min(minimum, intervals[i][0])
                maximum = max(maximum, intervals[i][1])
            else :
                final_array.append([minimum, maximum])
                minimum = intervals[i][0]
                maximum = intervals[i][1]
        final_array.append([minimum, maximum])
        return final_array