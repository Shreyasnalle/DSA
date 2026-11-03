class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]] :
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = []
        def backtracking(index, addition, arr) :
            if addition > n or len(arr) > k :
                return
            if addition == n :
                if len(arr) == k :
                    result.append(arr.copy())
                return
            if index >= 9 :
                return
            arr.append(nums[index])
            backtracking(index + 1, addition + nums[index], arr)
            arr.pop()
            backtracking(index + 1, addition, arr)
        backtracking(0, 0, [])
        return result