def reversePairs(nums: list[int]) -> int:
    count = 0
    n = len(nums)
    for i in range(n) : 
        for j in range(i, n) :
            if nums[i] > 2 * nums[j] :
                count += 1
    return count
final = reversePairs([2, 4, 3, 5, 1])
print(final)

class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        def merge_sort(left, right):
            if left >= right:
                return 0
            mid = (left + right) // 2
            count = merge_sort(left, mid) + merge_sort(mid + 1, right)
            j = mid + 1
            for i in range(left, mid + 1):
                while j <= right and nums[i] > 2 * nums[j]:
                    j += 1
                count += (j - (mid + 1))
            nums[left:right + 1] = sorted(nums[left:right + 1])
            return count
        return merge_sort(0, len(nums) - 1)
