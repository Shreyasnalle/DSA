class Solution :
    def countFrequencies(self, nums : list) -> list :
        frequency = {}
        for num in nums :
            if num in frequency :
                frequency[num] += 1
            else :
                frequency[num] = 1
        arr= []
        for (element, value) in frequency.items() :
            arr.append([element, value])
        print(arr)
object = Solution()
object.countFrequencies([1, 2, 2, 1, 3])