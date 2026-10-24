def generateBinaryStrings(n: int) -> list[str]:
    result = []
    def backtrack(current_str):
        if len(current_str) == n:
            result.append(current_str)
            return
        backtrack(current_str + "0")
        if not current_str or current_str[-1] != '1':
            backtrack(current_str + "1")
    backtrack("")
    return result
print(generateBinaryStrings(3))
print(generateBinaryStrings(2))