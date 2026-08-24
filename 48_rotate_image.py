class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        for r in range(len(matrix)):
            subarray = matrix[r]
            for c in range(r + 1, len(subarray)):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
        for r in range(len(matrix)):
            subarray = matrix[r]
            subarray.reverse()