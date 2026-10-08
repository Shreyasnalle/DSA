class Solution:
    def findPeakGrid(self, mat: list[list[int]]) -> list[int]:
        m = len(mat)        
        n = len(mat[0])
        low = 0
        high = n - 1
        while low <= high:
            mid_col = (low + high) // 2
            max_row = 0
            for r in range(m):
                if mat[r][mid_col] > mat[max_row][mid_col]:
                    max_row = r

            curr = mat[max_row][mid_col]
            if mid_col - 1 >= 0 :
                left = mat[max_row][mid_col - 1]
            else :
                left = -1
            if mid_col + 1 < n :
                right = mat[max_row][mid_col + 1]
            else :
                right = -1
            
            if curr > left and curr > right:
                return [max_row, mid_col]
            elif left > curr:
                high = mid_col - 1 
            else:
                low = mid_col + 1

        return []