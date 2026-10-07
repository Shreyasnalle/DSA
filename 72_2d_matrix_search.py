class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        def binary_searching_in_rows(m, target) :
            low = 0
            high = len(m) - 1
            while low <= high :
                mid = (low + high) // 2
                if m[mid] == target :
                    return 1
                if m[mid] < target :
                    low = mid + 1
                else :
                    high = mid + 1
            return -1

        n = len(matrix)
        for i in range(n) :
            m = matrix[i]
            vaani = binary_searching_in_rows(m, target)
            if vaani == 1 :
                return True
        return False
# time complexity is O(nlogm), n becuase the function of binary_searching_in_rows is being called inside a for loop of n

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        low = 0
        high = (rows * columns) - 1
        while low <= high :
            mid = (low + high) // 2
            if matrix[mid // columns][mid % columns] == target :
                return True
            elif matrix[mid // columns][mid % columns] < target :
                low = mid + 1
            else :
                high = mid - 1
        return False
# here the 2d array is converted into 1d array and the time complexity is O(log(row*columns))