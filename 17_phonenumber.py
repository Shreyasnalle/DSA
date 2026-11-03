class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits :
            return []
        numberletter = {
            2 : "abc",
            3 : "def",
            4 : "ghi",
            5 : "jkl",
            6 : "mno",
            7 : "pqrs",
            8 : "tuv",
            9 : "wxyz"
        }
        result = [""]
        for digit in digits :
            letters = numberletter[int(digit)]
            temp = []
            for combination in result :
                for letter in letters :
                    temp.append(combination + letter)
            result = temp
        return result

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits :
            return []
        numberletter = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        result = []
        def backtracking(index, arr):
            if index == len(digits):
                result.append("".join(arr))
                return
            letters = numberletter[int(digits[index])]
            for letter in letters:
                arr.append(letter)
                backtracking(index + 1, arr)
                arr.pop()
        backtracking(0, [])
        return result