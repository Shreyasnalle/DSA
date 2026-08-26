class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        output = []
        for i in range(numRows) :
            if i == 0 :
                output.append([1])
            elif i == 1 :
                output.append([1, 1])
            else :
                rough = output[i - 1]
                demo = [1, 1]
                for j in range(len(rough) - 1) :
                    addition = rough[j] + rough[j + 1]
                    demo.insert(j + 1, addition)
                output.append(demo)
        return output