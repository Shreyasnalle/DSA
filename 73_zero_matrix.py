class Solution:
    def setZeroes(self, matrix : list[list[int]]) -> None :
        zero_subarray_position = []
        zero_position_in_subarray = []
        for r in range(len(matrix)) :
            subarray = matrix[r]
            for c in range(len(subarray)) :
                number = subarray[c]
                if number == 0 :
                    zero_subarray_position.append(r)
                    zero_position_in_subarray.append(c)
        for r in range(len(matrix)) :
            subarray = matrix[r]
            if r in zero_subarray_position :
                for c in range(len(subarray)) :
                    subarray[c] = 0
            else:
                for c in range(len(subarray)) :
                    if c in zero_position_in_subarray :
                        subarray[c] = 0