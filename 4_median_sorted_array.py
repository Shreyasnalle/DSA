class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        array = nums1 + nums2
        def merge(arr, low, mid, high):
            temp = []
            left = low
            right = mid + 1
            while left <= mid and right <= high:
                if arr[left] <= arr[right]:
                    temp.append(arr[left])
                    left += 1
                else:
                    temp.append(arr[right])
                    right += 1
            while left <= mid:
                temp.append(arr[left])
                left += 1
            while right <= high:
                temp.append(arr[right])
                right += 1
            for i in range(len(temp)):
                arr[low + i] = temp[i]
        def mergesort(arr, low, high):
            if low >= high:
                return
            mid = (low + high) // 2
            mergesort(arr, low, mid)
            mergesort(arr, mid + 1, high)
            merge(arr, low, mid, high)
        if len(array) > 0:
            mergesort(array, 0, len(array) - 1)
        length = len(array)
        mid = length // 2
        if length % 2 != 0:
            return float(array[mid])
        else:
            return (array[mid - 1] + array[mid]) / 2.0