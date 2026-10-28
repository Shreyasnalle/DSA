
class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        n = len(candidates)
        result = []
        def calculate(index, arr, current_sum) :
            if current_sum == target :
                result.append(arr.copy())
                return
            if index >= n or current_sum > target :
                return
            arr.append(candidates[index])
            calculate(index + 1, arr, current_sum + candidates[index])
            arr.pop()
            while index + 1 < n and candidates[index] == candidates[index + 1] :
                index += 1
            calculate(index + 1, arr, current_sum)
        calculate(0, [], 0)
        return result