class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def finding_the_target_inside_the_matrix(row, target) :
            low = 0 
            high = len(row) - 1
            while low <= high :
                mid = (low + high) // 2
                if row[mid] == target :
                    return True
                elif row[mid] > target :
                    high = mid - 1
                else :
                    low = mid + 1
            return False

        n = len(matrix)
        for row in matrix :
            if finding_the_target_inside_the_matrix(row, target) :
                return True
        return False
# the time complexity of this question is O(nlogm)

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        row = 0
        col = cols - 1
        while row < rows and col >= 0:
            val = matrix[row][col]
            if val == target:
                return True
            elif val > target:
                col -= 1 
            else:
                row += 1
        return False 
# the time complexity of this code is O(m+n)