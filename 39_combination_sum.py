class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def calculate(arr, index, current_sum):
            if current_sum == target:
                result.append(arr.copy())
                return
            if current_sum > target or index == len(candidates):
                return
            arr.append(candidates[index])
            calculate(arr, index, current_sum + candidates[index])
            arr.pop()
            calculate(arr, index + 1, current_sum)
        calculate([], 0, 0)
        return result