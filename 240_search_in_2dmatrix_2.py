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