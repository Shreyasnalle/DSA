class Solution:
    def partition(self, s: str) -> list[list[str]]:
        result = []
        def backtracking(index, arr) :
            if index == len(s):
                result.append(arr.copy())
                return
            for i in range(index, len(s)) :
                temp = s[index:i+1]
                if temp == temp[::-1] :
                    arr.append(temp)
                    backtracking(i + 1, arr)
                    arr.pop()
        backtracking(0, [])
        return result